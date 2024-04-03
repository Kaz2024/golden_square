from lib.greet import *

def test_greet_return_hello():
    result = greet("Kathey")
    assert result ==  "Hello, Kathey!"
