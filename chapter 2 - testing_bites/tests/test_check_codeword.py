from lib.check_codeword import *

def test_check_codeword():
    assert check_codeword ("horse") == "Correct! Come in."
    assert check_codeword ("water") == "WRONG!"
    assert check_codeword ("house") == "Close, but nope."
