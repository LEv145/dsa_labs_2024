# noinspection GrazieInspection
r"""
8(3(1,6(4,7)),10(,14(13,)))

        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

Лабораторная работа №17: Реализация операций над бинарным деревом поиска (БДП): поиск, добавление, удаление.
Требования:
    - Дерево вводится в программу в формате линейно-скобочной записи.
    - Программа должна предоставить меню с операциями:
        - Добавление вершины в БДП.
        -Удаление вершины из БДП.
        - Поиск вершины в БДП.
    - После выполнения операции программа возвращается в меню.
    - При выходе из меню, перед завершением программы, на экран должно быть выведено БДП любым способом (линейно-скобочная запись или графическая форма).

"""
from common import Node, parse_tree


def search_bst(node: Node | None, key: int) -> Node | None:
    """
    Функция ищет узел с заданным ключом key в бинарном дереве поиска.

    Алгоритм использует свойство БДП:
    для каждого узла все значения в левом поддереве меньше его значения, а в правом поддереве — больше.
    """

    if node is None or node.value == key:
        return node
    elif key < node.value:
        return search_bst(node.left, key)
    else:
        return search_bst(node.right, key)


def insert_bst(node: Node | None, key: int) -> Node | None:
    """
    Функция вставляет новый узел с ключом key в бинарное дерево поиска.

    Алгоритм рекурсивно спускается по дереву,
    пока не найдёт подходящее место для вставки нового узла, сохраняя свойства БДП.
    """

    if node is None:
        return Node(key)
    elif key < node.value:
        node.left = insert_bst(node.left, key)
    elif key > node.value:
        node.right = insert_bst(node.right, key)
    else:
        print("Такой элемент уже существует в дереве.")
    return node


def delete_bst(root: Node | None, key: int) -> Node | None:
    """
    Функция удаляет узел с заданным ключом key из бинарного дерева поиска.

    Алгоритм обрабатывает три основных случая:
        - Узел для удаления — лист (не имеет детей).
        - Узел для удаления имеет одного ребёнка.
        - Узел для удаления имеет двух детей.
    """

    if root is None:
        return root

    if key < root.value:
        root.left = delete_bst(root.left, key)
    elif key > root.value:
        root.right = delete_bst(root.right, key)
    else:
        # Узел с одним или без детей
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Узел с двумя детьми
        temp = find_min_node(root.right)
        root.value = temp.value
        root.right = delete_bst(root.right, temp.value)
    return root


def find_min_node(node: Node | None) -> Node | None:
    current = node
    while current.left is not None:
        current = current.left
    return current


def tree_to_string(node: Node | None) -> str:
    if node is None:
        return ""

    left_str = tree_to_string(node.left)
    right_str = tree_to_string(node.right)
    result = str(node.value)
    if left_str or right_str:
        result += "(" + left_str
        result += "," + right_str
        result += ")"

    return result


def choice_option_in_menu():
    print("\nМеню:")
    print("1. Поиск элемента в БДП")
    print("2. Добавление элемента в БДП")
    print("3. Удаление элемента из БДП")
    print("4. Выход и вывод дерева")
    choice = input("Выберите действие (1-4): ")
    return choice


def main() -> None:
    tree_str = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
    root = parse_tree(tree_str)

    while True:
        choice = choice_option_in_menu()
        if choice == "1":
            key = int(input("Введите значение для поиска: "))

            result = search_bst(root, key)
            if result:
                print(f"Элемент {key} найден в дереве.")
            else:
                print(f"Элемент {key} не найден в дереве.")
        elif choice == "2":
            key = int(input("Введите значение для добавления: "))

            root = insert_bst(root, key)
            print(f"Элемент {key} добавлен в дерево.")
        elif choice == "3":
            key = int(input("Введите значение для удаления: "))

            root = delete_bst(root, key)
            print(f"Элемент {key} удалён из дерева.")
        else:
            print("Итоговое дерево в линейно-скобочной записи:")
            print(tree_to_string(root))
            break


if __name__ == "__main__":
    main()
