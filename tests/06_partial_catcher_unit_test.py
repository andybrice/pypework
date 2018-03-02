from pypework import PartialCatcher
from functions import *

## Unit Tests ##

class TestPartialCatcher(object):
    def test_exists(self):
        assert PartialCatcher

    def test_instantiates_with_no_arguments(self):
        f = PartialCatcher()
        assert f.__class__ == PartialCatcher

    def test_instantiates_with_named_scope(self):
        f = PartialCatcher( scope = __name__ )
        assert f.__class__ == PartialCatcher

    def test_scope_named(self):
        current_module = __import__(__name__)
        f = PartialCatcher( scope = __name__ )
        assert f._identifier_chain == current_module

    def test_scope_automatic(self):
        current_module = __import__(__name__)
        f = PartialCatcher()
        assert f._identifier_chain == current_module
