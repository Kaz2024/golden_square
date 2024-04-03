from lib.report_length import *

def test_report_length():
    result = report_length("Hi")
    assert result == "This string was 2 characters long."