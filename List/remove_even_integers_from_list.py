# Implement a function that removes all the even elements from a given list. Name it remove_even(lst).

# Solution

# Manual Solution

# Time complexity: O(n)
# Space Complexity: O(1)
def remove_even(lst):
    odds = []

    for num in lst:
        if num % 2 != 0:
            odds.append(num)

    return odds


# Pythonic Solution
def remove_even_pythonic(lst):
    return [num for num in lst if num % 2 != 0]


def remove_even_filter(lst):
    return list(filter(lambda n: n % 2 != 0, lst))


if __name__ == "__main__":
    print(remove_even([1, 2, 4, 5, 10, 6, 3]))
    print(remove_even_pythonic([1, 2, 4, 5, 10, 6, 3]))
    print(remove_even_filter([1, 2, 4, 5, 10, 6, 3]))