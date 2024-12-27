# 3.2.1.15 LAB: Queue aka FIFO
class QueueError(Exception):  # Custom exception for Queue errors
    pass

class Queue:
    def __init__(self):
        self.__storage = []  # Internal list to store the elements

    def put(self, elem):
        self.__storage.append(elem)  # Add element to the end of the list

    def get(self):
        if not self.__storage:  # Check if the queue is empty
            raise QueueError("Queue is empty")  # Raise QueueError if empty
        return self.__storage.pop(0)  # Remove and return the first element

# Testing the Queue class
que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):  # Attempt to retrieve 4 elements
        print(que.get())
except QueueError:
    print("Queue error")
