from pypework import FunctionCatcher
from functions import *

## Unit Tests ##

class TestFunctionCatcher:
    def test_exists(self):
        assert FunctionCatcher

    def test_instantiates_with_no_arguments(self):
        f = FunctionCatcher()
        assert f.__class__ == FunctionCatcher

    def test_instantiates_with_named_scope(self):
        f = FunctionCatcher( scope = __name__ )
        assert f.__class__ == FunctionCatcher

    def test_scope_named(self):
        current_module = __import__(__name__)
        f = FunctionCatcher( scope = __name__ )
        assert f._identifier_chain == current_module

    def test_scope_automatic(self):
        current_module = __import__(__name__)
        f = FunctionCatcher()
        assert f._identifier_chain == current_module
