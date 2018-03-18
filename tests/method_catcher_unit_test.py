from pypework import MethodCatcher#, resolve_identifier_chain
from functions import *
from types import SimpleNamespace
import pytest

def test_exists():
    assert MethodCatcher

def test_instantiates():
    m = MethodCatcher()
    assert m.__class__ == MethodCatcher

def test_scope():
    mock_scope = ['foo', 'bar']
    m = MethodCatcher(scope=mock_scope)
    assert m._scope == mock_scope

def test_catches_method():
    m = MethodCatcher()
    x = m.foo.bar
    assert x._scope == ['foo', 'bar']

@pytest.fixture
def bob():
    return SimpleNamespace(
        name = 'Bob',
        date_of_birth = SimpleNamespace(
            year = 1989,
            month = 9,
            day = 21
        )
    )

# def test_resolve_identifier_chain(bob):
#     x = resolve_identifier_chain(bob, ['name'])
#     assert x == 'Bob'

# def test_resolve_identifier_chain_recursive(bob):
#     x = resolve_identifier_chain(bob, ['date_of_birth', 'day'])
#     assert x == 21

def test_invokes(bob):
    m = MethodCatcher()
    d = m.name
    x = d.invoke_on(bob)
    
    assert x == 'Bob'

def test_invokes_recursively(bob):
    m = MethodCatcher()
    d = m.date_of_birth.day
    x = d.invoke_on(bob)
    
    assert x == 21