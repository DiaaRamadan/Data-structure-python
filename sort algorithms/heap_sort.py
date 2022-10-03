def heap_sort(items: list):
    for j in range(0, len(items) // 2 - 1):
        heapify(items, len(items), j)

    for index in range(len(items) - 1, 0, -1):
        items[index], items[0] = items[0], items[index]
        heapify(items, index, 0)


def heapify(items, size, index):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < size and items[index] < items[left_index]:
        largest = left_index

    if right_index < size and items[largest] < items[right_index]:
        largest = right_index

    if largest != index:
        items[index], items[largest] = items[largest], items[index]
        heapify(items, size, largest)


arr = [12, 11, 13, 5, 6, 7, ]
heap_sort(arr)
n = len(arr)
print('Sorted array is')
print(arr)
for i in range(n):
    print(arr[i])
