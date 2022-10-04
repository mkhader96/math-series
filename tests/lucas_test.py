import pytest
from math_series.math_series import lucas

def test_zero():
    actual=lucas(0)
    expected=2
    assert actual == expected

def test_one():
    actual=lucas(1)
    expected=1
    assert actual == expected

def test_two():
    actual=lucas(2)
    expected=3
    assert actual == expected

def test_three():
   actual=lucas(3)
   expected=4
   assert actual == expected 

def test_four():
   actual=lucas(4)
   expected=7
   assert actual == expected 

def test_five():
    actual=lucas(5)
    expected=11
    assert actual == expected 