#!/usr/bin/env python

"""Tests for the `nbex.paths` module."""

import pytest
from pathlib import Path

import nbex
import nbex.interactive
from nbex.paths import get_package_path


def test_get_package_path_returns_path_for_package():
    assert isinstance(get_package_path(nbex), Path)


def test_get_package_path_returns_path_for_module():
    assert isinstance(get_package_path(nbex.interactive), Path)


def test_get_package_raises_error_for_non_package_arg():
    with pytest.raises(ValueError):
        get_package_path("Not a package.")
