from pathlib import Path


def get_package_path(package):
    """Compute the file-system path for `package`."""
    if hasattr(package, "__path__"):
        return Path(package.__path__[0])
    elif hasattr(package, "__file__"):
        return Path(package.__file__).parent
    else:
        raise ValueError(f"Cannot determine path for package {package}")
