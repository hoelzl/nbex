#!/usr/bin/env python

"""Tests for the `nbex.interactive` module."""

from nbex.interactive import (
    Session,
    session,
    display_interactive,
    print_interactive,
    pprint_interactive,
)

# The following two tests assume the interpreter is not running in interactive
# mode.

def test_python_is_interactive_returns_false():
    assert Session().python_is_interactive is False


def test_session_initializes_is_interactive_to_false():
    assert Session().is_interactive is False


# TODO: maybe add a test that launches an interactive python interpreter and
# checks that session.is_interactive is true in there?


def test_session_can_be_set_to_non_interactive():
    session.is_interactive = False
    assert not session.is_interactive


def test_session_can_be_set_to_interactive():
    session.is_interactive = True
    assert session.is_interactive


def test_display_interactive_generates_no_output_when_session_not_interactive(
    capsys,
):
    session.is_interactive = False
    display_interactive("Hello")
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_display_interactive_generates_output_when_session_interactive(capsys):
    session.is_interactive = True
    display_interactive("Hello")
    out, err = capsys.readouterr()
    assert "Hello" in out
    assert not err


def test_pprint_interactive_generates_no_output_when_session_not_interactive(
    capsys,
):
    session.is_interactive = False
    pprint_interactive("Hello")
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_pprint_interactive_generates_output_when_session_interactive(capsys):
    session.is_interactive = True
    pprint_interactive([1, 2])
    out, err = capsys.readouterr()
    assert out == "[1, 2]\n"
    assert not err


def test_pprint_interactive_pretty_prints_output(capsys):
    session.is_interactive = True
    # Generate a list that is long enough to trigger line breaks between
    # elements.
    pprint_interactive(list(range(1, 40)))
    out, err = capsys.readouterr()
    # Generate the output list: all elements but the last are followed by a
    # comma and a linebreak, each element except for the first is indented one
    # space.
    assert out == "[" + ",\n ".join(map(str, range(1, 40))) + "]\n"
    assert not err


def test_print_interactive_generates_no_output_when_session_not_interactive(
    capsys,
):
    session.is_interactive = False
    print_interactive("Hello")
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_print_interactive_generates_output_when_session_interactive(capsys):
    session.is_interactive = True
    print_interactive([1, 2])
    out, err = capsys.readouterr()
    assert out == "[1, 2]\n"
    assert not err
