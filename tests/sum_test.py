import pytest
from math_series.math_series import sum

def test_zero_fib():
    actual=sum(0)
    expected=0
    assert actual == expected

def test_zero_lucas():
    actual=sum(0,2,1)
    expected=2
    assert actual == expected

def test_zero_random():
    actual=sum(0,3,3)
    expected=3
    assert actual == expected

def test_one_fib():
    actual=sum(1)
    expected=1
    assert actual == expected
    
def test_one_lucas():
    actual=sum(1,2,1)
    expected=1
    assert actual == expected

def test_one_random():
    actual=sum(1,4,5)
    expected=5
    assert actual == expected

def test_two_fib():
    actual=sum(2,0,1)
    expected=1
    assert actual == expected

def test_two_lucas():
    actual=sum(2,2,1)
    expected=3
    assert actual == expected

def test_two_random():
    actual=sum(2,4,6)
    expected=10
    assert actual == expected

def test_three_fib():
   actual=sum(3,0,1)
   expected=2
   assert actual == expected 

def test_three_lucas():
   actual=sum(3,2,1)
   expected=4
   assert actual == expected 

def test_three():
   actual=sum(3,3,3)
   expected=9
   assert actual == expected 

def test_string():
    actual=sum("test")
    expected= "Please Enter a Number"
    assert actual == expected