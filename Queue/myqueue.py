from dll import DoublyLinkedList


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()
        self.size = 0

    def front(self):
        return self.items.get_head()

    def rear(self):
        return self.items.get_tail()

    def enqueue(self, data):
        self.size += 1
        return self.items.insert_at_tail(data)

    def dequeue(self):
        self.size -= 1
        return self.items.remove_head()

    def __str__(self):
        return str(self.items)


# driver code
if __name__ == "__main__":
    queue = MyQueue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print("Front", queue.front())
    print("Back", queue.rear())
    queue.dequeue()
    queue.dequeue()
    # queue.dequeue()
    print(queue)

