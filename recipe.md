# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
def find_item_in_to_do(notes):
    # finds task #TODO in line in notes -> notes is a string
    # return -> boolean value TRUE or FALSE
    # side effects? none! (hopefully)

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
>>> test no string ("")
    False
>>> test string ("no key word")
    False
>>> test string ("#TODO stuff")
    True
>>> test string("TODO things")
    False
>>> test lower false ("#todo other things")
    False
>>> test in middle ("iwant#TODOEVERYTHING")
    True



>>> includes_todo("#TODO buy milk")
True
>>> includes_todo("drink tea")
False
>>> includes_todo("learn to test-drive my code #TODO")
True


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
