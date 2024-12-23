"""
Merge sort

Худшее время: O(nlogn)
Лучшее время: O(nlogn)
Среднее время: O(nlogn)
"""


def merge_sort(lst: list[int]):
    if len(lst) <= 1:
        return lst

    # Разделяй
    middle = len(lst) // 2
    print(1, lst[:middle], lst[middle:])
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    print(2, left, right)

    # Влавствуй
    l = 0
    r = 0
    k = 0
    tmp = [0] * len(lst)
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            tmp[k] = left[l]
            l += 1
        else:
            tmp[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        tmp[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        tmp[k] = right[r]
        r += 1
        k += 1

    for i in range(len(lst)):
        lst[i] = tmp[i]
    return lst


def main():
    lst = [6, 5, 3, 1, 8, 7, 2, 4]
    lst = merge_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()