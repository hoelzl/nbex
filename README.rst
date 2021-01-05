=========================
Notebook-like Executables
=========================


.. image:: https://img.shields.io/pypi/v/nbex.svg
        :target: https://pypi.python.org/pypi/nbex

.. image:: https://img.shields.io/travis/hoelzl/nbex.svg
        :target: https://travis-ci.com/hoelzl/nbex

.. image:: https://readthedocs.org/projects/nbex/badge/?version=latest
        :target: https://nbex.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/hoelzl/nbex/shield.svg
     :target: https://pyup.io/repos/github/hoelzl/nbex/
     :alt: Updates



Python programs that allow notebook-like development.


* Free software: MIT license
* Documentation: https://nbex.readthedocs.io.


Features
--------

* Switch between development and deployment modes

  * Use development mode to configure smaller data tables, models, etc.

  * Use deployment mode to run full deployment and training

* Switch between interactive and command-line usage

  * Use interactive mode to interact with the code in a notebook, receive styled IPython output, etc.

  * Use command-line usage to run the code in your CI system, etc.

Installation for Development
----------------------------

To develop `nbex` with a standard Python environment install it as

.. code-block:: bash

  pip install -e .

from the root directory of the package.

If you are using conda, make sure that you have the `conda-build` package installed
and then install `nbex` with

.. code-block:: bash

  conda develop .

from the root directory of the package.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
