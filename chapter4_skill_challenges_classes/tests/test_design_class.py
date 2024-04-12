from lib.design_class import *
import pytest 


def test_initally_has_no_task():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []


# """
# when we add a task
# it reflects in the list 
# """
def test_add_task_reflect_the_task():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    assert tracker.list_incomplete() == ["walk the dog"]

# """
# adding multiple tasks
# it reflects all in the list 
# """

def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    tracker.add("Drink water")
    tracker.add("check in online")
    assert tracker.list_incomplete() == [
        "walk the dog", "Drink water","check in online" ]

# ```
# adding multiple tasks
# it reflects all in the list and marks the one as complete
# it disappeared from th etask list 
# """
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    tracker.add("Drink water")
    tracker.add("check in online")
    tracker.mark_complete(1)
    assert tracker.list_incomplete()== ["walk the dog", "check in online"]


# ```
# if we try to mark a track complete that does not exist
# it raises an error

# """

def test_mark_task_that_is_too_low_to_complet():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1)
        assert str(err.value) == "No such task to mark complete"
        assert tracker.list_incomplete() == ["walk the dog"]
    # tracker.mark_complete(2) => raises an error 
    # tracker.list_incomplete() == ["walk the dog"]

def test_mark_task_that_is_too_high_to_complet():
    tracker = TaskTracker()
    tracker.add("walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(4)
        assert str(err.value) == "No such task to mark complete"
        assert tracker.list_incomplete() == ["walk the dog"]

# tracker = TaskTracker()
# tracker.add("walk the dog")
# tracker.mark_complete(2) => raises an error 
# tracker.list_incomplete()
# ["walk the dog"]