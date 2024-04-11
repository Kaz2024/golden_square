from lib.grammar_stats import *
import pytest 

def test_empty_text_raise_error():
    with pytest.raises(Exception) as err:
        GrammarStats("")
        assert str(err.value)  == "Error! User must enter a text."

def test_string_with_capital_letter_and_a_full_stop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello world.")
    assert result == True 

def test_good_grammmar_percentage_of_the_text():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello world.")
    grammar_stats.check("jello world.")
    grammar_stats.check("Hello world")
    grammar_stats.check("Hello world!")
    assert grammar_stats.percentage_good()== 50
    
