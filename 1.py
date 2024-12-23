
SUPPORTED_SYM = {"{": "}", "[": "]", "(": ")"}


def main():
    input_ = input("Введите строку: ")

    lst = list(input_)
    if check_lst(lst):
        print("Строка существует")
    else:
        print("Строка не существует")


def check_lst(lst: list):
    print(lst)
    if not lst:
        return True

    while lst:
        results = []

        first_item_index = 0
        second_item = SUPPORTED_SYM.get(lst[first_item_index])
        if second_item is None:  # ")("
            return False
        counter = 0

        for index, item in enumerate(lst):
            if second_item is None:
                continue

            if item == lst[first_item_index]:
                counter += 1

            if item == second_item:
                counter -= 1

            if item == second_item and counter == 0:
                results.append(lst[first_item_index+1:index])

                if index >= len(lst)-1:
                    continue

                first_item_index = index+1
                second_item = SUPPORTED_SYM.get(lst[first_item_index])
                if second_item is None:  # ")("
                    return False
                counter = 0

        if counter != 0:
            # "["
            return False

        return all(
            check_lst(result)
            for result in results
        )

    return True


if __name__ == "__main__":
    main()
