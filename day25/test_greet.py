import pytest
from greet import greet

def test_greet_alice() -> None:
    assert greet("Alice") == "Hello, Alice!"

def test_greet_bob() -> None:
    assert greet("Bob") == "Hello, Bob!"


