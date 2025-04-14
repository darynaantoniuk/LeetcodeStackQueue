"""Maximum Frequency Stack"""


class Node:
    """node"""
    def __init__(self, value):
        self.value = value
        self.next = None


class MyStack:
    """MyStack"""
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
        popped = self.top.value
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
        return self.top.value


class FreqStack:
    """
    class FreqStack
    """
    def __init__(self):
        """
        init method
        """
        self.freq_map = {}
        self.group_map = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        push method
        """
        if val in self.freq_map:
            self.freq_map[val] += 1
        else:
            self.freq_map[val] = 1

        freq = self.freq_map[val]

        if freq not in self.group_map:
            self.group_map[freq] = MyStack()
        self.group_map[freq].push(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        """
        pop method
        """
        val = self.group_map[self.max_freq].pop()
        self.freq_map[val] -= 1
        if self.group_map[self.max_freq].is_empty():
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
