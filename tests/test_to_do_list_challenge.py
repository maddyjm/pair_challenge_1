from lib.to_do_list_challenge import *

def test_no_string_returns_false():
    assert find_item_in_to_do("") == False

def test_no_todo_returns_false():
    assert find_item_in_to_do("no key word") == False

def test_todo_in_string_returns_true():
    assert find_item_in_to_do("#TODO stuff") == True

def test_todo_no_hashtag_returns_false():
    assert find_item_in_to_do("TODO things") == False

def test_lowercase_returns_false():
    assert find_item_in_to_do("#todo other things") == False

def test_in_middle_returns_true():
    assert find_item_in_to_do("iwant#TODOEVERYTHING") == True