from importlib.resources import files

def load_static_file(name: str) -> str:
    """Load static file from the ``virtualship.static`` module by file name."""
    return files("my_package.static").joinpath(name).read_text(encoding="utf-8")
