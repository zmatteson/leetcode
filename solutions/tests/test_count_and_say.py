import pytest
from solutions.count_and_say import *
# input of one should return "one"
def test_one_returns_one_one():
    x = get_sequence(1)
    assert x == 1