from lib.gratitudes import *

# gratitude in a list 
def test_gratitude_in_a_list():
    gratitude_list = Gratitudes()
    assert gratitude_list.gratitudes == []

# add gratitude in the list
def test_add_gratitude_to_the_list():
    gratitude_list = Gratitudes()
    gratitude_list.add ("someone")
    gratitude_list.add ("friends")
    assert gratitude_list.format ( )== "Be grateful for: someone, friends"


# def test_formatted_gratitude_list():
