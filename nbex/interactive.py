# %% [markdown]
#
# # Support for interactive sessions
#
# We want to use the code both in interactive session where we want more
# output, etc., and for batch processing. This file contains utilities for
# writing code that outputs interesting information when being run
# interactively without being annoying when batch processing data.

# %%
import sys
import inspect
from IPython.core.display import display
from pprint import pprint


class Session:
    """Control behavior in interactive vs. batch mode"""

    def __init__(self) -> None:
        self.forced_interactive_value = None

    @property
    def python_is_interactive(self) -> bool:
        return hasattr(sys, "ps1")

    @staticmethod
    def _find_first_non_nbex_stack_frame():
        caller_frame = inspect.currentframe().f_back

        # Walk up at most 100 stack frames to find one that is not from
        # nbex.interactive
        for _ in range(100):
            if caller_frame.f_globals["__name__"] == "nbex.interactive":
                caller_frame = caller_frame.f_back
            else:
                break
        else:
            raise UserWarning("Walked 100 stack frames inside nbex.interactive?")

        return caller_frame

    @property
    def _is_called_from_main(self):
        caller_frame = self._find_first_non_nbex_stack_frame()
        return caller_frame.f_globals["__name__"] == "__main__"

    @property
    def is_interactive(self) -> bool:
        if self.forced_interactive_value is None:
            return self._is_called_from_main and self.python_is_interactive
        else:
            return self.forced_interactive_value


session = Session()


def display_interactive(
    *objs,
    include=None,
    exclude=None,
    metadata=None,
    transient=None,
    display_id=None,
    **kwargs
):
    """Display `obj` when in interactive mode."""
    if session.is_interactive:
        display(
            *objs,
            include=include,
            exclude=exclude,
            metadata=metadata,
            transient=transient,
            display_id=display_id,
            **kwargs
        )


def pprint_interactive(
    object,
    stream=None,
    indent=1,
    width=80,
    depth=None,
    *,
    compact=False,
    sort_dicts=True
):
    """Pretty-print `obj` when in interactive mode."""
    if session.is_interactive:
        pprint(
            object,
            stream=stream,
            indent=indent,
            width=width,
            depth=depth,
            compact=compact,
            sort_dicts=sort_dicts,
        )


def print_interactive(*obj: object):
    """Print `obj` when in interactive mode."""
    if session.is_interactive:
        print(*obj)


# %%
