class QueueArray:
    def __init__(self, size=None):
        self.capacity = 10 if size is None else size
        self.array = [None] * self.capacity
        self.head = -1
        self.tail = -1

    def enqueue(self, item):
        # check if queue is full
        if(self.tail + 1) % self.capacity == self.head:
            raise Exception("Queue is full")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity

        self.array[self.tail] = item

    def dequeue(self):
        if self.head == -1:
            raise Exception("Queue is empty")

        item = self.array[self.head]
        self.array[self.head] = None
        
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        
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
