"""
Поразрядная сортировка

Худшее время: O(k*n)
"""


BASE = 10


def radix_sort(lst: list[int]) -> list[int]:
    max_len = max(len(str(i)) for i in lst)

    for place in range(max_len):
        tmp_lists: list[list[int]] = [[], [], [], [], [], [], [], [], [], []]
        for num in lst:
            digit = (num // BASE**place) % BASE

            tmp_lists[digit].append(num)

        lst = [item for tmp_list in tmp_lists for item in tmp_list]

    return lst


def main():
    print("Список 1")
    lst = [137137105157, 24395739293, 474290561035, 5, 276, 42]
    lst = radix_sort(lst)
    print(lst)
    print("Список 2")
    lst = [32, 95, 16, 82, 24, 66, 35, 19, 75, 54, 40, 43, 93, 68]
    lst = radix_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
