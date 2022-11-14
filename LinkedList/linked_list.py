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

    def is_empty(self):
        return self.__head_node is None

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
    linked_list.insert_at_head(3)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(1)
    linked_list.insert_at_tail(4)
    linked_list.insert_at_tail(5)
    linked_list.insert_at_head(10)

    print(linked_list)
