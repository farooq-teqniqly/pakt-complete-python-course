"""
A simple stack.
"""


class Stack:
    """
    A simple stack.
    """

    def __init__(self):
        """
        Creates a new Stack instance.
        """
        self.items = []

    def push(self, *items):
        """
        Adds items to the stack.
        Args:
            *items: The items to add.
        """

        self.items.extend(items)

    def pop(self):
        """
        Removes an item from the stack.
        Returns:
        The removed item.
        """

        if not self.items:
            return None

        tail = self.items[-1]
        self.items = self.items[:-1]
        return tail


s = Stack()
s.push(1, 2, 3)
s.push(1, 2, 3)

while s.items:
    v = s.pop()
    print(v)
