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


def pre_order_non_recursive(root: Node | None) -> str:
    """Pre-order non recursive.

    Алгоритм:
        1. Инициализировать пустой стек и поместить в него корень дерева.
        2. Пока стек не пуст:
            - Извлечь узел из стека.
            - Посетить узел (добавить его значение в строку обхода).
            - Если у узла есть правый ребенок, поместить его в стек.
            - Если у узла есть левый ребенок, поместить его в стек.
        3. Повторять, пока все узлы не будут посещены.

    Важно: Мы помещаем правый ребенок перед левым, чтобы левый узел был на вершине стека и обрабатывался первым.
    """
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(str(node.value))

        # Поскольку стек работает по принципу LIFO, мы сначала добавляем правый узел
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return " ".join(result)


def pre_order_non_recursive_2(root: Node | None) -> str:
    result = []
    stack = [root]

    while stack:
        node = stack.pop(0)
        result.append(str(node.value))

        if node.left:
            stack.insert(0, node.left)
        if node.right:
            stack.insert(1, node.right)

    return " ".join(result)


def main():
    input_string = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
    root = parse_tree(input_string)

    print("Нерекурсивный прямой обход (Pre-order):")
    print(pre_order_non_recursive(root))


if __name__ == "__main__":
    main()
