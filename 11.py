"""
Quick sort

Худшее время: O(nlogn)
Лучшее время: O(nlogn)
Среднее время: O(nlogn)
"""


def quick_sort(lst: list[int]):
    x, xs = lst[0], lst[1:]
    if not lst:
        return []

    return (
        quick_sort([i for i in xs if i < x])
        + [x]
        + quick_sort([i for i in xs if i >= x])
    )

quick_sort = lambda lst: [] if not lst else quick_sort([i for i in lst[1:] if i < lst[0]]) + [lst[0]] + quick_sort([i for i in lst[1:] if i >= lst[0]])


def main():
    print("Список 1")
    lst = [137137105157, 24395739293, 474290561035, 5, 276, 42]
    lst = quick_sort(lst)
    print(lst)
    print("Список 2")
    lst = [32, 95, 16, 82, 24, 66, 35, 19, 75, 54, 40, 43, 93, 68]
    lst = quick_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
