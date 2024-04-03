from lib.counter import *

# def test_counter():
#     counter = Counter("2")
#     counter.count = ("8")
#     result = counter.count()
#     assert result == "Counted to 8 so far"

def test_counter_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_a_single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == ("Counted to 5 so far.")

def test_counter_adds_mtltiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == ("Counted to 8 so far.")