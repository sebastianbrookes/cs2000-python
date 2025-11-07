import pytest

from day25.pyret_to_python_practice import (
    double,
    is_even,
    greet,
    square,
    starts_with_a,
)


def test_double_basic():
    assert double(0) == 0
    assert double(10) == 20
    assert double(-3) == -6


def test_double_float():
    assert double(2.5) == 5.0


def test_is_even():
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(7) is False
    assert is_even(-4) is True


def test_greet():
    assert greet("Ada") == "Hello, Ada!"
    assert greet("") == "Hello, !"


def test_square():
    assert square(0) == 0
    assert square(5) == 25
    assert square(-3) == 9
    assert square(2.5) == 6.25


def test_starts_with_a():
    assert starts_with_a("apple") is True
    assert starts_with_a("Apple") is True
    assert starts_with_a("banana") is False
    assert starts_with_a("") is False

