#!/usr/bin/env python

"""Tests for the `nbex.dev_mode` module."""

import nbex.dev_mode  # noqa: F401
from nbex.interactive import session


def test_dev_mode_can_be_set_to_false():
    session.dev_mode = False
    assert session.dev_mode is False


def test_dev_mode_can_be_set_to_true():
    session.dev_mode = True
    assert session.dev_mode is True


def test_default_dev_mode_table_size_is_1000():
    assert session.dev_mode_table_size == 1000


def test_pandas_table_size_is_available():
    assert "pandas_table_size" in dir(session)


def test_pandas_table_size_returns_size_in_dev_mode():
    session.dev_mode = True
    assert session.pandas_table_size == session.dev_mode_table_size


def test_pandas_table_size_returns_none_in_production_mode():
    session.dev_mode = False
    assert session.pandas_table_size is None
