# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker():

    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass 

    def list_incomplete(self):
        # Returns:
        #   A list of incomplete tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass 

    def mark_complete(self, index):
        # Parameters:
        #   index: an interger representing the task to complete
        # Returns:
        #   A list of complete tasks
        # Side-effects:
        #   Tremoves the task at index from the list of tasks 
        pass 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially there are no tasks 

"""
tracker = TaskTracker()
tracker.list_incomplete() => []



"""
when we add a task
it reflects in the list 
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.list_incomplete() => ["walk the dog"]

"""
adding multiple tasks
it reflects all in the list 
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.add("Drink water")
tracker.add("check in online")
tracker.list_incomplete() => ["walk the dog", "Drink water","check in online" ]

```
adding multiple tasks
it reflects all in the list and marks the one as complete
it disappeared from th etask list 
"""
tracker = TaskTracker()
tracker.add("walk the dog")
tracker.add("Drink water")
tracker.add("check in online")
tracker.mark_complete(1) => 
tracker.list_incomplete()
["walk the dog", "check in online" ]

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
