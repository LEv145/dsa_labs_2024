"""
Сортировка Шелла

Худшее O(n^2)
Лучшее O(nlog^2n)

1. Выбираются шаги
2. Сортируем вставками каждые элементы, отличающиеся на шаг (Сортировка вставками со step)
"""


def shell_sort(lst: list[int]) -> list[int]:
    steps = get_steps(len(lst))

    for step in steps:
        for start in range(step):
            # Сортировка вставками со step
            for i in range(start+step, len(lst), step):
                for j in range(i, step-1, -step):
                    if lst[j] < lst[j-step]:
                        lst[j], lst[j-step] = lst[j-step], lst[j]
                    else:
                        break

    return lst


def get_steps(N: int) -> list[int]:
    # Последовательность, предложенная Шеллом
    d = int(N / 2)
    lst = [d]
    while d > 1:
        d = int(d / 2)
        lst.append(d)
    return lst


if __name__ == "__main__":
    lst = [32, 95, 16, 82, 24, 66, 35, 19, 75, 54, 40, 43, 93, 68]
    lst = shell_sort(lst)
    print(lst)