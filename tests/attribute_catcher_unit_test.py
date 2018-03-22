from pypework import AttributeCatcher#, resolve_identifier_chain
from functions import *
from types import SimpleNamespace
import pytest

def test_exists():
    assert AttributeCatcher

def test_instantiates():
    m = AttributeCatcher()
    assert m.__class__ == AttributeCatcher

def test_chain():
    mock_chain = ['foo', 'bar']
    m = AttributeCatcher(chain=mock_chain)
    assert m._chain == mock_chain

## Fixtures ##

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def greet(self, greeting="Hello"):
        return greeting + ", " + self.name + "!"

@pytest.fixture
def alice():
    return Person(
        name = 'Alice',
        date_of_birth = SimpleNamespace(
            year = 1991,
            month = 4,
            day = 7
        )
    )

@pytest.fixture
def bob():
    return Person(
        name = 'Bob',
        date_of_birth = SimpleNamespace(
            year = 1989,
            month = 9,
            day = 21
        )
    )

@pytest.fixture
def people():
    a = alice()
    b = bob()
    return [a,b]

## Attributes ##

def test_catches_attributes_recursively():
    m = AttributeCatcher()
    x = m.foo.bar
    assert x._chain[0]._attribute_name == 'foo'
    assert x._chain[1]._attribute_name == 'bar'

def test_invokes(bob):
    n = AttributeCatcher().name
    x = n._invoke_on(bob)
    
    assert x == bob.name

def test_invokes_recursively(bob):
    d = AttributeCatcher().date_of_birth.day
    x = d._invoke_on(bob)
    
    assert x == bob.date_of_birth.day

## Subscripts ##

def test_subscripts(people):
    a = AttributeCatcher()[0]
    x = a._invoke_on(people)

    assert x == people[0]

## Calls ##

def test_calls(alice):
    a = AttributeCatcher().greet()
    x = a._invoke_on(alice)

    assert x == alice.greet()

## Chains ##

def test_chains(people):
    a = AttributeCatcher()[0].name.upper()
    x = a._invoke_on(people)

    assert x == people[0].name.upper()