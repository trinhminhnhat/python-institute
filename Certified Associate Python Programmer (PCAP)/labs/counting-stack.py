# 3.2.1.14 Counting stack
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()  # Initialize the parent class
        self.__counter = 0  # Initialize the private counter

    def get_counter(self):
        return self.__counter  # Return the current value of the counter

    def pop(self):
        # Override the pop method to update the counter
        val = super().pop()  # Call the parent class's pop method
        self.__counter += 1  # Increment the counter
        return val


# Test the class
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())
