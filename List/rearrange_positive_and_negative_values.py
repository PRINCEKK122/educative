# Implement a function rearrange(lst) which rearranges the elements such that all
# the negative elements appear on the left and positive elements appear at the right of the list.
# Note that it is not necessary to maintain the sorted order of the input list.

# pythonic solution
def rearrange(lst):
    # time complexity - O(n)
    return [n for n in lst if n < 0] + [n for n in lst if n >= 0]



# manual solution
def rearrange_2(lst):
    # time complexity - O(n)
    results = []

    for n in lst:
        if n < 0:
            results.append(n)

    for n in lst:
        if n >= 0:
            results.append(n)

    return results


if __name__ == "__main__":
    print(rearrange([10, -1, 20, 4, 5, -9, -6]))
    print(rearrange_2([10, -1, 20, 4, 5, -9, -6]))