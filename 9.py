"""
Пирамидальная сортировка (Сортировка кучей)

Худшее  O(nlogn)
Среднее O(nlogn)
Лучшее  O(nlogn)
"""


def heap_sort(lst: list):
    """Сортировка кучей."""
    # Представим, что нам массив - дерево, где
    # Левый потомок: 2*i + 1
    # Правый потомок: 2*i + 2

    # Формируем первоначальное сортирующее дерево
    # Для этого справа-налево перебираем элементы массива c потомками -> В просейку
    for start in range((len(lst) - 2) // 2, -1, -1):
        heap_sift(lst, start, len(lst) - 1)

    # Первый элемент массива всегда соответствует корню сортирующего дерева
    # и поэтому является максимумом для неотсортированной части массива.
    for end in range(len(lst)-1, 0, -1):
        # Меняем этот максимум местами с последним элементом неотсортированной части массива
        lst[end], lst[0] = lst[0], lst[end]

        # Восстанавливаем сортирующее дерево (Просейка для неотсортированной части массива)
        heap_sift(lst, 0, end - 1)
    return lst


def heap_sift(lst, start_index, lst_end_index):
    """Просейка свеху вниз."""
    root_index = start_index

    while True:
        # Левый индекс потомока
        child_index = root_index * 2 + 1

        # Нет потомков
        if child_index > lst_end_index:
            break

        # Среди обоих потомков выбираем наибольший (Выбираем правого потомка, иначе - левого)
        if (
            child_index + 1 <= lst_end_index  # Правый потомок в приделе массива
            and lst[child_index] < lst[child_index + 1]  # Правый потомок больше
        ):
            child_index = child_index + 1  # Выбираем правого потомка

        # Если больший потомок больше корня, то меняем местами,
        if lst[root_index] < lst[child_index]:
            lst[root_index], lst[child_index] = lst[child_index], lst[root_index]
            root_index = child_index  # Больший потомок - новый кровень
        # Конец просейки
        else:
            break


def main():
    print("Список 1")
    lst = [137137105157, 24395739293, 474290561035, 5, 276, 42]
    lst = heap_sort(lst)
    print(lst)
    print("Список 2")
    lst = [32, 95, 16, 82, 24, 66, 35, 19, 75, 54, 40, 43, 93, 68]
    lst = heap_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()