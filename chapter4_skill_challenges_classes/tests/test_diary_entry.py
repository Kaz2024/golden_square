from lib.diary_entry import *
import pytest
# Given an empty title and contents
# Return an error 

def test_empty_string_return_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
        assert str(err.value) == "Diary entries must have a title or contents."


# Given a title and contents
#format returns a formatted entry, like:
# "My Title: These are the contents"

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

# given a title and content
# count words returns the number of words in the title and contents

def test_gets_count_of_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

# Give the title and contents
# return the reading per minute 

def test_reading_estimate():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

# Given a word per minute of 2 
# and a text with 4 words 
# return 2 minutes

def test_reading_estimate():
    diary_entry = DiaryEntry("My Title", "Some contents two three")
    result = diary_entry.reading_time(2)
    assert result == 2
