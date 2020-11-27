from nbex.interactive import session, Session


session.dev_mode = session.is_interactive
session.dev_mode_table_size = 1000


class PandasTableSize:
    """Return the desired number of rows of a pandas table.

    Returns different values for dev mode and production mode."""

    def __get__(self, session, objtype=None):
        if session.dev_mode:
            return session.dev_mode_table_size
        else:
            return None


_pandas_table_size = PandasTableSize()
setattr(Session, "pandas_table_size", _pandas_table_size)
