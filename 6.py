"""
Сортировка выбором

Худшее:  O(n^2)
Лучшее:  O(n^2)
Среднее: O(n^2)

1. Находим минимальный элемент
2. Производим обмен этого элемента с элементом первой неотсортированной позиции
3. Сортируем хвост
"""


def selection_sort(lst: list[int]) -> list:
    for head_index in range(len(lst)-1):
        min_index = search_min_index(lst, start=head_index)
        lst[head_index], lst[min_index] = lst[min_index], lst[head_index]
    return lst


def search_min_index(lst: list[int], start: int = 0) -> int:
    index = start
    for i in range(start, len(lst)):
        if lst[i] < lst[index]:
            index = i
    return index


if __name__ == "__main__":
    lst = [2, 4, 1, 5, 7, 8, 1, 2, 4, 7, 9, 0, 1, 3, -2]
    lst = selection_sort(lst)
    print(lst)
