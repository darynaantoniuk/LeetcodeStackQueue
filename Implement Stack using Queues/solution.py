"""Implement stack using queues"""


class Node:
    """node"""
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    """MyQueue"""
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def enqueue(self, value):
        """enqueue"""
        new_node = Node(value)

        if self.rear:
            self.rear.next = new_node
        self.rear = new_node

        if not self.front:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        """dequeue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None

        self.size -= 1
        return dequeued

    def peek(self):
        """peek"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        dequeued = self.front.value
        return dequeued

    def is_empty(self):
        """is empty"""
        return self.front is None

    def get_size(self):
        """get size"""
        return self.size


class MyStack:
    """
    MyStack class
    """
    def __init__(self):
        """
        init method
        """
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()

    def push(self, x: int) -> None:
        """
        push method
        """
        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1.enqueue(x)
        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

    def pop(self) -> int:
        """
        pop method
        """
        if self.empty():
            raise IndexError("Pop from empty stack")
        return self.queue1.dequeue()

    def top(self) -> int:
        """
        top method
        """
        if self.empty():
            raise IndexError("Top from empty stack")
        return self.queue1.peek()

    def empty(self) -> bool:
        """
        empty method
        """
        return self.queue1.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
