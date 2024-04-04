import pytest
from lib.present import *


# def test_the_content():
#     pass

def test_present():
    present = Present("Me")
    with pytest.raises(Exception) as e:
        present.wrap()
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
