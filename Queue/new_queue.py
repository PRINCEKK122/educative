from Stack.stack import Stack

class NewQueue:
    def __init__(self):
        self.__main_stack = Stack()
        self.__temp_stack = Stack()

    def enqueue(self, value):
        self.__main_stack.push(value)

    def dequeue(self):
        if self.__main_stack.is_empty() and self.__temp_stack.is_empty():
            return None

        # transfer all items from the main_stack to the temp_stack
        while self.__main_stack.is_empty() is False:
            self.__temp_stack.push(self.__main_stack.pop())

        temp = self.__temp_stack.pop()

    def __str__(self):
        return str(self.__main_stack)


if __name__ == "__main__":
    queue = NewQueue()
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(3)
    print("queue", queue)
    item = queue.dequeue()
    print(item)
    print("new queue", queue)