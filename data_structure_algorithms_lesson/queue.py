"""
A simple queue.
"""


class Queue:
    """
    A simple queue.
    """

    def __init__(self):
        """
        Creates a new Queue instance.
        """
        self.items = []

    def push(self, *items):
        """
        Adds items to the queue.
        Args:
            *items: The items to add.
        """
        self.items.extend(items)

    def pop(self):
        """
        Removes an item from the queue.
        Returns:
        The removed item.
        """
        if not self.items:
            return None

        head = self.items[0]
        self.items = self.items[1:]
        return head


q = Queue()
q.push(1, 2, 3)
q.push(1, 2, 3)

while q.items:
    print(q.pop())
