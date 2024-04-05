from lib.password_checker import *
import pytest 

def test_check_pasword_is_greater_than_8():
    checker = PasswordChecker()
    password = "12345678"
    assert checker.check(password) == True

def test_check_password_less_than_8():
    checker = PasswordChecker()
    password = "1234567"
    with pytest.raises(Exception) as e:
        checker.check(password)
    error_message = str(e.value)
    assert error_message == "Invaild password, must be 8+ characters."