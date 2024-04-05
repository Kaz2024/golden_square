from lib.string_builder import *

"""
the output of an empty string
"""
def test_inital_output_as_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

# add the str 

def test_add_string_output_that_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    assert stringbuilder.output() == "hello"

# it should return the length of the string 
def test_length_of_the_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("world")
    assert stringbuilder.size() == 5

#adding multiple strings so they will join together 
def test_multiple_string_join_together():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    stringbuilder.add(" ")
    stringbuilder.add("world")
    assert stringbuilder.output()=="hello world"

# the size of the multiple string 

def test_the_size_of_the_multiple_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    stringbuilder.add(" ")
    stringbuilder.add("world")
    assert stringbuilder.size() == 11