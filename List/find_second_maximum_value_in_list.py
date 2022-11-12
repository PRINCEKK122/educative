# Implement a function find_second_maximum(lst) which returns the second largest element in the list.

def find_second_maximum(lst):
    # time complexity - O(nlogn)
    # space complexity - O(1)
    if len(lst) == 0:
        return None

    if len(lst) == 1:
        return lst[0]

    lst.sort()

    return lst[-2]



def find_second_maximum_2(lst):
    max_num = second_max_num = float("-inf")

    for i in range(len(lst)):
        if lst[i] > max_num:
            second_max_num = max_num
            max_num = lst[i]
        elif lst[i] < max_num and lst[i] > second_max_num:
            second_max_num = lst[i]

    return second_max_num


if __name__ == "__main__":
    print(find_second_maximum([9, 5, 2, 6, 17]))
    print(find_second_maximum_2([9, 5, 2,100,  6, 17]))
