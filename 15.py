r"""
8(3(1,6(4,7)),10(,14(13,)))

        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
"""
from common import Node, parse_tree


def pre_order(node: Node | None) -> None:
    """Прямой обход (Pre-order).

    Алгоритм:
        - Посетить текущий узел.
        - Рекурсивно обойти левое поддерево.
        - Рекурсивно обойти правое поддерево.

    Пояснение:
        - Сначала обрабатываем текущий узел (node.value).
        - Затем рекурсивно обходим левое и правое поддеревья.
    """
    if node is not None:
        print(node.value, end=" ")
        pre_order(node.left)
        pre_order(node.right)


def in_order(node: Node | None) -> None:
    """Центральный обход (In-order).

    Алгоритм:
        - Рекурсивно обойти левое поддерево.
        - Посетить текущий узел.
        - Рекурсивно обойти правое поддерево.

    Пояснение:
        - Сначала обходим левое поддерево.
        - Затем обрабатываем текущий узел.
        - После этого обходим правое поддерево.
    """
    if node is not None:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)


def post_order(node: Node | None) -> None:
    """Концевой обход (Post-order).

    Алгоритм:
        - Рекурсивно обойти левое поддерево.
        - Рекурсивно обойти правое поддерево.
        - Посетить текущий узел.

    Пояснение:
        - Сначала обходим левое и правое поддеревья.
        - Затем обрабатываем текущий узел.
    """
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end=' ')


def main() -> None:
    input_string = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
    root = parse_tree(input_string)

    print("Прямой обход (Pre-order):")
    pre_order(root)
    print()

    print("Центральный обход (In-order):")
    in_order(root)
    print()

    print("Концевой обход (Post-order):")
    post_order(root)
    print()


if __name__ == "__main__":
    main()
