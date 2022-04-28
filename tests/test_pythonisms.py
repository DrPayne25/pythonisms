from pythonisms import __version__
from pythonisms.stack import Stack, Node

import pytest


def test_for_in():
    # ['apple'] -> ['banannana'] - > ['cucumber'] -> None
    foods = Stack(("apple","banana","cucumber"))
    foods_list = [] 
    for food in foods:
        foods_list.append(food)
    assert foods_list == ["cucumber","banana","apple"]

def test_node_instance():
    node = Node(1,None)
    assert node.next == None
    assert node.data == 1

#Test One Push onto a stack
def test_stack_push_one():
    stack = Stack()
    stack.push('1')
    assert stack.top.data == '1'

def test_stack_push_one_wrong():
    stack = Stack()
    stack.push('2')
    assert stack.top.data != '3'
#Test 2 Push multiple datas onto a stack
def test_stack_push_multiple():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    assert stack.top.data == '6'

def test_stack_push_multiple_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    assert stack.top.data != '2'
#Test 3 pop off stack
def test_stack_pop_one():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    assert stack.top.data == '4'

def test_stack_pop_one_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    assert stack.top.data != '6'
#Test 4 empty a stack after multiple pops
def test_stack_pop_all():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_stack_pop_all_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top != '6'

#Test 5 Peek the next item on a stack
def test_peek_stack():
    stack = Stack()
    stack.push('2')
    assert stack.peek() == '2'

# @pytest.mark.skip('Pending')
def test_peek_stack_not_working():
    stack = Stack()
    stack.push('2')
    assert stack.peek() != '3'

#Test 6 instantiate an empty stack
def test_empty_stack():
    stack = Stack()
    actual = stack.isEmpty()
    expected = True
    assert actual == expected

def test_empty_stack_not_working():
    stack = Stack()
    stack.push('2')
    actual = stack.isEmpty()
    expected = True
    assert actual != expected

#Test 7 Calling pop or peek on empty stack raises exception
def test_peek_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()

def test_pop_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()

