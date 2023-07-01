class StackArray:
    def __init__(self, size=None):
        self.capacity = 10 if size is None else size
        self.array = [None] * self.capacity
        self.top = -1

    def push(self, item):
        if (self.top + 1) == self.capacity:
            raise Exception("Capacity reached, unable to add more items")

        self.top += 1
        self.array[self.top] = item
        
    def pop(self):
        if self.top < 0:
            raise Exception("Stack is empty, no items to return")

        item = self.array[self.top]
        self.array[self.top] = None
        self.top -= 1

        return item

    def size(self):
        count = 0
        for item in self.array:
            if item is not None:
                count += 1

        return count

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return str(self.array)
