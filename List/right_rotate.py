# Implement a function right_rotate(lst, k) which will rotate the given list by k.
# This means that the right-most elements will appear at the left-most position in the list and so on.
# You only have to rotate the list by one element at a time.


# pythonic solution
def right_rotate(lst, k):
    # time complexity - O(n)
    # space complexity - O(1)
    offset = k % len(lst)

    # get all the elements from the end and append it to the remaining elements
    return lst[-offset:] + lst[:-offset]


# manual approach
def right_rotate_2(lst, k):
    # time-complexity - O(n)
    # space complexity - O(n)
    results = []
    offset = k % len(lst)

    for i in range(len(lst) - offset, len(lst)):
        results.append(lst[i])

    for i in range(len(lst) - offset):
        results.append(lst[i])

    return results

if __name__ == "__main__":
    print(right_rotate(["right", "rotate", "python"], 4))
    print(right_rotate_2(["right", "rotate", "python"], 4))