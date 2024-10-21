from importlib.resources import files

def load_static_file(name: str) -> str:
    return files("my_package.static").joinpath(name).read_text(encoding="utf-8")

print(load_static_file("example.txt"))
