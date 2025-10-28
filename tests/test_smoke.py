import importlib

def test_import_main():
    module = importlib.import_module("main")
    assert module is not None
