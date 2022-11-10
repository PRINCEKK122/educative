# In this problem, you have to implement the find_sum(lst,k)
# function which will take a number k as input and return two numbers that add up to k.


# Solution 1
def find_sum(lst, k):
    if len(lst) < 2:
        return None

    lst.sort()
    left_idx = 0
    right_idx = len(lst) - 1

    while left_idx < right_idx:
        summation = lst[left_idx] + lst[right_idx]

        if summation == k:
            return [lst[left_idx], lst[right_idx]]
        elif summation < k:
            left_idx += 1
        else:
            right_idx -= 1

    return None


if __name__ == "__main__":
    print(find_sum([1,21,3,14,5,60,7,6], 13))