from myqueue import MyQueue

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


# Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first
# “k” elements of the queue. An illustration is also provided for your understanding.
def reverseK(queue: MyQueue, k):
    # Scenario 1 handles if the queue is empty, or if k is greater than size of queue, or if k is negative
    pass



if __name__ == "__main__":
    print(find_bin(9))
    print([0] * 10)
