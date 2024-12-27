# 3.2.1.16 Queue aka FIFO: part 2
class QueueError(Exception):  # Custom exception for Queue errors
    pass

class Queue:
    def __init__(self):
        self.__lst = []

    def put(self, elem):
        self.__lst.append(elem)

    def get(self):
        if not self.__lst:
            raise QueueError("Queue is empty")
        return self.__lst.pop(0)

class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__lst) == 0  # Access the private attribute


# Testing
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
