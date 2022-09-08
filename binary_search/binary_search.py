def binary_search(array, target):
    end_index = len(array) - 1
    start_index = 0

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_element = array[mid_index]
        if mid_element == target:
            return mid_index
        elif target < mid_element:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    return -1


def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)


print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))

print(binary_search_recursive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 0, 9))
