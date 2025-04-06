"""Implement Queue using Stacks"""


class Node:
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Stack"""
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        """push"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """pop"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped

    def is_empty(self):
        """is empty"""
        return self.top is None

    def peek(self):
        """peek"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data


class MyQueue:
    """MyQueue"""
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        """push"""
        self.stack_in.push(x)

    def pop(self) -> int:
        """pop"""
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        """peek"""
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        """empty"""
        return self.stack_in.is_empty() and self.stack_out.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
