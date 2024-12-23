"""
Сортировка расчесткой

Худшее: O(n^2)
Лучшее: O(nlogn)
Память O(1)
"""


def comb_sort(lst: list[int], factor: int = 1.25) -> list:
    n = len(lst)
    step = n - 1

    # Когда step == 1 равносильно одиному проходу сортировки пузырьком
    while step >= 1:
        for i in range(n):
            if i + step >= n:
                break

            if lst[i] > lst[i+step]:
                lst[i], lst[i+step] = lst[i+step], lst[i]

        step = int(step / factor)

    return lst


if __name__ == "__main__":
    lst = [2, 4, 1, 5, 7, 8, 1, 2, 4, 7, 9, 0, 1, 3, -2]
    lst = comb_sort(lst)
    print(lst)
