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


if __name__ == "__main__":
    print(find_bin(6))
