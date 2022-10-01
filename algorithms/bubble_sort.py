def bubble_sort(items: list):
    if len(items) < 0:
        raise Exception("Empty list")

    for i in range(1, len(items)):
        no_swap = True
        for j in range(0, len(items) - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                no_swap = False
        if no_swap:
            break


wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
bubble_sort(wakeup_times)
print(wakeup_times)
