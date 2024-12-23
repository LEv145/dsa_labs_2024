import typing as t


class Node:
    def __init__(self, value: t.Any):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self) -> str:
        left_value = self.left.value if self.left is not None else None
        right_value = self.right.value if self.right is not None else None
        return f"Node(V:{self.value!r} L:{left_value!r} R:{right_value!r})"


def parse_tree(string: str):
    string = string.replace(" ", "")  # 8(3(1,6(4,7)),10(,14(13,)))
    if not string:
        return None

    def parse_node(index: int) -> tuple[Node | None, int]:
        # Парсим число
        num = ""
        while index < len(string) and string[index].isdigit():
            num += string[index]
            index += 1

        if not num:
            return None, index

        node = Node(int(num))

        # Проверяем, есть ли дочерние узлы
        if index < len(string) and string[index] == "(":
            index += 1  # Пропускаем '('

            # Парсим левый ребёнок
            node.left, index = parse_node(index)

            index += 1  # Пропускаем ','

            # Парсим правый ребёнок
            node.right, index = parse_node(index)

            index += 1  # Пропускаем ')'

        return node, index

    root, _ = parse_node(0)
    return root
