def shunting_yard(expression: str) -> list:
    """Алгоритм shunting yard ля преобразования в постфикную запись"""

    output = []  # Выход
    operators = []  # Стек операторов
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Операции

    for token in expression.split():
        # Если число, то добавляем в результат
        if token.isdigit():
            output.append(token)

        # Если оператор
        elif token in precedence:
            while (
                operators  # Если список операторов не постуй
                and operators[-1] != "("  # Задерживаем, если ( в конце
                and precedence.get(operators[-1], 0) >= precedence[token]  # Задерживаем, если `приоритет последнего оператора` < `приоритеты текущего`
            ):
                output.append(operators.pop())
            operators.append(token)

        elif token == "(":
            operators.append(token)

        # Выход из порочного круга
        elif token == ")":
            # Выталкиваем остаток операторов, пока не встретим `(`
            while (
                operators   # Если список операторов не постуй
                and operators[-1] != "("  # Если последний оператор в очереди дейсвительно оператор
            ):
                output.append(operators.pop())

            # Удаляем `(`
            if (
                operators
                and operators[-1] == "("
            ):
                operators.pop()

    # Выталкиваем остаток операторов
    while operators:
        output.append(operators.pop())

    return output


def evaluate_postfix(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise RuntimeError("Деление на 0")

                stack.append(a / b)

    return stack[0]


if __name__ == "__main__":
    expression = "3 + 4 * 2 / ( 1 - 5 * ( 2 + 4 ) )="

    expression = expression.replace("=", "")  # Выкидываем мусор
    print(expression)
    postfix = shunting_yard(expression)  # ['3', '4', '2', '*', '1', '5', '-', '/', '+']
    print(postfix)
    result = evaluate_postfix(postfix)
    print(result)
