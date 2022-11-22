from dll import DoublyLinkedList


class Queue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def front(self):
        return self.items.get_head()

    def rear(self):
        return self.items.get_tail()

    def enqueue(self, data):
        return self.items.insert_at_tail(data)

    def dequeue(self):
        return self.items.remove_head()

# driver code
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.dequeue()
    queue.dequeue()
    # queue.dequeue()
    print(queue.items)

