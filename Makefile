.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 --max-line-length=88 nbex tests

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source nbex -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/nbex.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ nbex
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	pip -e install .

CONDA_DIST_FILES = \
	build/conda-build/linux-32/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-64/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-aarch64/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-armv6l/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-armv7l/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-ppc64/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-ppc64le/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-s390x/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/osx-64/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/osx-arm64/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/win-32/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/win-64/nbex-0.4.0-py38_1.tar.bz2 \
	build/conda-build/linux-32/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-64/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-aarch64/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-armv6l/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-armv7l/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-ppc64/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-ppc64le/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/linux-s390x/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/osx-64/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/osx-arm64/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/win-32/nbex-0.4.0-py39_1.tar.bz2 \
	build/conda-build/win-64/nbex-0.4.0-py39_1.tar.bz2

build/target-file-38:
	conda-build . --py 3.8 --output-folder build/conda-build --output > build/target-file-38

build/target-file-39:
	conda-build . --py 3.9 --output-folder build/conda-build --output > build/target-file-39

conda-release: build/target-file-37 build/target-file-38 build/target-file-39 ## package and upload a release for conda
	conda convert --platform all `cat build/target-file-38` -o build/conda-build
	conda convert --platform all `cat build/target-file-39` -o build/conda-build
	for item in $(CONDA_DIST_FILES); do anaconda upload --skip-existing $$item; echo "" > /dev/null; done

conda-dist: ## build anaconda packages
	conda-build --py 3.8 --py 3.9 --output-folder build/conda-build .

conda-install: clean ## install the package into the current conda environment
	conda develop .
