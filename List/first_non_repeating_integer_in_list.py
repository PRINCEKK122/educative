# Implement a function, find_first_unique(lst) that returns the first unique integer in the list.
def find_first_unique(lst):
    # time complexity - O(n^2) for the worse case when the non-duplicate number is the last element
    # space complexity - O(1)
    if len(lst) == 0:
        return None

    for i in range(len(lst)):
        found_duplicate = False

        for ele in lst[i+1:]:
            if lst[i] == ele:
                found_duplicate = True

        if not found_duplicate:
            return lst[i]