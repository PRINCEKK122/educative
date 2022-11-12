# Implement a function, find_product(lst), which modifies a list so that each index has a
# product of all the numbers present in the list except the number stored at that index.

# Brute force approach
def find_product(lst):
    # Time complexity = O(n^2)
    # Space complexity = O(1)
    size = len(lst)
    results = []

    for i in range(size):
        product = 1
        for j in range(size):
            if i != j:
                product *= lst[j]

        results.append(product)

    return results


def find_product_2(lst):
    # Time complexity - O(n)
    # Space complexity - O(1)
    results = []
    left = 1
    right = 1
    left_products = [1 for _ in lst]
    right_products = [1 for _ in lst]

    for i in range(len(lst)):
        left *= lst[i]
        left_products[i] = left

    for i in range(len(lst) - 1, -1, -1):
        right *= lst[i]
        right_products[i] = right

    for i in range(len(lst)):
        if i == 0:
            results.append(right_products[i + 1])
            continue
        if i == len(lst) - 1:
            results.append(left_products[i - 1])
            continue

        results.append(left_products[i - 1] * right_products[i + 1])

    return results


def find_product_3(lst):
    left = 1
    product = []

    for ele in lst:
        product.append(left)
        left *= ele
    print("Left product", product)
    right = 1
    for i in range(len(lst) - 1, -1 , -1):
        product[i]  = product[i] * right
        right = right * lst[i]

    return product


if __name__ == "__main__":
    print(find_product([1, 2, 3, 4]))
    print(find_product_2([1, 2, 3, 4]))
    print(find_product_3([1, 2, 3, 4]))
