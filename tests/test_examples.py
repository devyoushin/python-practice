import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def load_example(name: str):
    path = ROOT / "ops" / "examples" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    return module


def test_greet() -> None:
    module = load_example("01_hello.py")
    assert module.greet("python") == "hello, python"


def test_collections() -> None:
    module = load_example("03_collections.py")
    assert module.unique_sorted(["b", "a", "b"]) == ["a", "b"]
    assert module.count_by_name(["a", "a", "b"]) == {"a": 2, "b": 1}
