"""
Сортировка вставками

Худшее: O(n^2)
Лучшее: O(n)
"""


def insert_sort(lst: list[int]) -> list:
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break

    return lst


if __name__ == "__main__":
    lst = [2, 4, 1, 5, 7, 8, 1, 2, 4, 7, 9, 0, 1, 3, -2]
    lst = insert_sort(lst)
    print(lst)