# Implement a function findMinimum(lst) which finds the smallest number in the given list.

def findMinimum(lst):
    # time complexity - O(n)
    # Space complexity - O(1)
    min_value = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]

    return min_value


if __name__ == "__main__":
    print(findMinimum([9, 2, 3, 6]))