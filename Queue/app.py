from myqueue import MyQueue
from Stack.stack import Stack

def find_bin(number):
    result = []
    my_queue = MyQueue()
    my_queue.enqueue(1)
    for i in range(number):
        result.append(str(my_queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        my_queue.enqueue(s1)
        my_queue.enqueue(s2)

    return result


# Implement the function reverseK(queue, k) which takes a queue and a number âkâ as input and reverses the first
# âkâ elements of the queue.
def reverseK(queue: MyQueue, k):
    # Scenario 1 handles if the queue is empty, or if k is greater than size of queue, or if k is negative
    if k < 0 or k > queue.size or queue.size == 0:
        return None

    stack = Stack()

    for _ in range(k):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    for _ in range(queue.size - k):
        queue.enqueue(queue.dequeue())

    return queue




if __name__ == "__main__":
    # print(find_bin(9))
    my_queue = MyQueue()

    for i in range(15):
        my_queue.enqueue(i)

    print(reverseK(my_queue, 4))

    stack = Stack()
    stack.push(2)
    stack.push(97)
    stack.push(4)

    print("sort stack", sort_stack(stack))
    print(123497)
