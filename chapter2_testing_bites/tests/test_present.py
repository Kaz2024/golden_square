import pytest
from lib.present import *


def test_the_content():
    present=Present()
    present.wrap(33)
    assert present.unwrap()==33

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

#if wrap twice 
def test_if_wrap_twice():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."