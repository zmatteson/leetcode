import pytest
from solutions.count_and_say import *
# input of one should return "one"
def test_one_returns_one():
    x = get_sequence(1)
    assert x == 1

def test_two_returns_one_one():
    x = get_sequence(2)
    assert x == 11

def test_three_returns_21():
    x = get_sequence(3)
    assert x == 21

def test_four_returns_1211():
    x = get_sequence(4)
    assert x == 1211

def test_five_returns_111221():
    x = get_sequence(5)
    assert x == 111221
def test_six_returns_312211():
    x = get_sequence(6)
    assert x == 312211