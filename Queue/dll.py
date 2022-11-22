class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__head is None

    def get_head(self):
        if self.is_empty():
            return None

        return self.__head.data

    def get_tail(self):
        if self.is_empty():
            return None

        return self.__tail.data

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

        self.__size += 1

    def insert_at_head(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__head.prev = new_node
            new_node.next = self.__head
            self.__head = new_node

        self.__size += 1

    def remove_head(self):
        if self.is_empty():
            return False
        node_to_remove = self.__head
        if (self.__size == 1):
            self.__head = self.__tail = None
        else:
            self.__head = node_to_remove.next
            self.__head.prev = None
            node_to_remove.next = None
        self.__size -= 1
        return node_to_remove.data

    def remove_tail(self):
        if self.is_empty():
            return None
        node_to_remove = self.__tail
        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            self.__tail = node_to_remove.prev
            node_to_remove.prev = None
            self.__tail.next = None

        return node_to_remove.data

    def __len__(self):
        return self.__size

    def __str__(self):
        result = []
        if self.is_empty() is None:
            return "DoublyLinkedList is empty!"

        current_node = self.__head

        while current_node is not None:
            result.append(str(current_node.data) + "-><-")
            current_node = current_node.next

        result.append("None")
        return "".join(result)


# driver code
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_tail(1)
    dll.insert_at_tail(2)
    dll.insert_at_tail(3)
    dll.insert_at_head(0)
    dll.insert_at_head(20)
    dll.insert_at_head(15)
    print("Head", dll.remove_head())
    print("Tail", dll.remove_tail())
    print("Size " + str(len(dll)))
    print(dll)
