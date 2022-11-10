# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
# Name it merge_lists(lst1, lst2).



# Solution
def merge_lists(lst1, lst2):
    # Time complexity is O(3n) which evaluates to O(n)
    # Space complexity is O(n)

    # starting index for both lists: lst1 and lst2
    index_1 = 0
    index_2 = 0
    index = 0
    sorted_lists = []

    while (index_1 < len(lst1)) and (index_2 < len(lst2)):
        if lst1[index_1] < lst2[index_2]:
            sorted_lists.append(lst1[index_1])
            index_1 += 1
        else:
            sorted_lists.append(lst2[index_2])
            index_2 += 1

        index += 1

    # if there are remaining elements in either list append them to sorted lists
    while index_1 < len(lst1):
        sorted_lists.append(lst1[index_1])
        index_1 += 1
        index += 1

    while index_2 < len(lst2):
        sorted_lists.append(lst2[index_2])
        index_2 += 1
        index += 1

    return sorted_lists


# merging in place
def merging_in_place(lst1, lst2):
    # Time complexity - O(n^2)
    # space complexity - O(1)
    idx_1 = 0
    idx_2 = 0

    while (idx_1 < len(lst1)) and (idx_2 < len(lst2)):
        if lst1[idx_1] > lst2[idx_2]:
            lst1.insert(idx_1, lst2[idx_2])
            idx_1 += 1
            idx_2 += 1
        else:
            idx_1 += 1


    if idx_2 < len(lst2):
        lst1.extend(lst2[idx_2:])

    return lst1

if __name__ == "__main__":
    print(merge_lists([4, 10],[1, 2, 3, 5]))
    print(merging_in_place([4, 5, 6], [-2, -1, 0, 7]))
