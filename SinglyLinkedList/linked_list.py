from SinglyLinkedList.node import Node


class SinglyLinkedList:
    def __init__(self):
        self.__head_node = None
        self.__size = 0

    def get_head(self):
        return self.__head_node

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.__head_node
        self.__head_node = new_node

        self.__size += 1
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

        self.__size += 1
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

            self.__size += 1
        return

    def search(self, value):
        node = self.__head_node

        while node is not None:
            if node.data == value:
                return True
            node = node.next

        return False

    def delete_at_head(self):
        if self.is_empty():
            print("Linked list is empty")
            return

        head_node = self.get_head()
        self.__head_node = head_node.next
        head_node.next = None

        self.__size -= 1

    def remove_duplicates(self):
        if self.is_empty():
            return

        if self.get_head().next is None:
            return self

        outer_node = self.__head_node

        while outer_node is not None:
            inner_node = outer_node

            while inner_node is not None:
                # found a duplicate
                if inner_node.next is not None:
                    if outer_node.data == inner_node.next.data:
                        next_node = inner_node.next.next
                        inner_node.next = next_node
                    else:
                        inner_node = inner_node.next
                else:
                    inner_node = inner_node.next
            outer_node = outer_node.next

        return self

    def union(self, linked_list2):
        if self.is_empty():
            return linked_list2
        elif linked_lists2.is_empty():
            return self

        start_node = self.__head_node

        while start_node.next is not None:
            start_node = start_node.next

        start_node.next = linked_lists2.get_head()
        return self.remove_duplicates()

    def delete_by_value(self, value):
        if not self.is_empty():
            current_node = self.get_head()
            previous_node = None

            if current_node.data == value:
                self.delete_at_head()
                return

            while current_node is not None:
                if current_node.data == value:
                    previous_node.next = current_node.next
                    current_node.next = None
                    break

                previous_node = current_node
                current_node = current_node.next

            self.__size -= 1

    def reverse_linked_list(self):
        if self.is_empty():
            print("Linked list is empty!")
            return

        previous_node = None
        current_node = self.get_head()

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

            self.__head_node = previous_node


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

    def __len__(self):
        return self.__size


if __name__ == "__main__":
    # linked_list = SinglyLinkedList()
    # linked_list.insert_at_head(3)
    # linked_list.insert_at_head(2)
    # linked_list.insert_at_head(1)
    # linked_list.insert_at_tail(4)
    # linked_list.insert_at_tail(5)
    # linked_list.insert_at(3, 10)
    # linked_list.insert_at_head(10)
    # linked_list.insert_at_head(10)
    # linked_list.insert_at_head(10)
    # linked_list.insert_at_head(10)
    # print(linked_list)
    # # linked_list.delete_at_head()
    # linked_list.delete_by_value(1)
    # # linked_list.reverse_linked_list()
    # print(linked_list)
    # print("Value found", linked_list.search(10))
    # print("Value found", linked_list.search(-1))
    # print(len(linked_list))
    # print("remove duplicates", linked_list.remove_duplicates())

    # print(linked_list)

    linked_lists1 = SinglyLinkedList()
    linked_lists1.insert_at_tail(1)
    linked_lists1.insert_at_tail(2)
    linked_lists1.insert_at_tail(3)

    linked_lists2 = SinglyLinkedList()
    linked_lists2.insert_at_tail(4)
    linked_lists2.insert_at_tail(5)
    linked_lists2.insert_at_tail(6)
    linked_lists2.insert_at_tail(4)

    linked_lists1.union(linked_lists2)
    print(linked_lists1)
