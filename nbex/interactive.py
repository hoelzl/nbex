# %% [markdown]
#
# # Support for interactive sessions
#
# We want to use the code both in interactive session where we want more
# output, etc., and for batch processing. This file contains utilities for
# writing code that outputs interesting information when being run
# interactively without being annoying when batch processing data.

from IPython.core.display import display
from pprint import pprint


class Session:
    """Control behavior in interactive vs. batch mode"""

    def __init__(self) -> None:
        self.is_interactive = False


session = Session()


def display_interactive(obj: object):
    """Display `obj` when in interactive mode."""
    if session.is_interactive:
        display(obj)


def pprint_interactive(obj: object):
    """Pretty-print `obj` when in interactive mode."""
    if session.is_interactive:
        pprint(obj)


def print_interactive(*obj: object):
    """Print `obj` when in interactive mode."""
    if session.is_interactive:
        print(*obj)
