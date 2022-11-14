from LinkedList.node import Node


class SinglyLinkedList:
    def __init__(self):
        self.__head_node = None

    def get_head(self):
        return self.__head_node

    def insert_at_head(self, data):
        new_node = Node(data)

        new_node.next = self.__head_node
        self.__head_node = new_node
        return self.__head_node

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.__head_node = new_node
            return

        node = self.get_head()

        while node.next is not None:
            node = node.next

        node.next = new_node
        return self.__head_node

    def insert_at(self, index, data):
        if index < 0:
            raise IndexError("Index cannot be negative")

        new_node = Node(data)
        if index == 0:
            self.insert_at_head(data)
        else:
            current_node = self.get_head()
            i = 0

            while i < index - 1:
                current_node = current_node.next
                i += 1

            next_node = current_node.next
            current_node.next = new_node
            new_node.next = next_node
        return

    def search(self, value):
        node = self.__head_node

        while node is not None:
            if node.data == value:
                return True
            node = node.next

        return False

    def is_empty(self):
        return self.get_head() is None

    def __str__(self):
        result = ""
        current_node = self.__head_node

        while current_node.next is not None:
            result += str(current_node.data) + " -> "
            current_node = current_node.next

        result += str(current_node.data) + " -> None"

        return result


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    print("is empty", linked_list.is_empty())
    linked_list.insert_at_head(3)
    print("is empty", linked_list.is_empty())
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(1)
    linked_list.insert_at_tail(4)
    linked_list.insert_at_tail(5)
    linked_list.insert_at(7, 10)
    print("Value found", linked_list.search(10))
    print("Value found", linked_list.search(-1))

    print(linked_list)
