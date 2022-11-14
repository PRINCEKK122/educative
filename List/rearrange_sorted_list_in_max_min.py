# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list
# such that the 0th index will have the largest number, the 1st index will have the smallest,
# and the 2nd index will have second-largest, and so on.
# In other words, all the even-numbered indices will have the largest numbers in the list in descending
# order and the odd-numbered indices will have the smallest numbers in ascending order.

def max_min(lst):
    # time complexity - O(n)
    # space complexity - O(n)
    left_idx = 0
    right_idx = len(lst) - 1
    results = []

    while left_idx < right_idx:
        results.append(lst[right_idx])
        results.append(lst[left_idx])

        left_idx += 1
        right_idx -= 1

        if len(lst) % 2 != 0:
            results.append(lst[left_idx])

    return results


if __name__ == "__main__":
    print(max_min([1, 2, 3, 4, 5]))