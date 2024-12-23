from pathlib import Path
import string


def djb2_hash(key: str) -> int:
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash_value * 33 + ord(char)
    return hash_value & 0xFFFFFFFF  # Ограничение в 32 бит


class HashTableOpenAddressing:
    """Хеш-таблица с открытой адресацией (Линейное пробирование)."""

    def __init__(self, size: int) -> None:
        self._size = size
        self._table = [None] * size

    def insert(self, key: str) -> None:
        index = djb2_hash(key) % self._size
        original_index = index
        while self._table[index] is not None:
            # Уже существует в таблице
            if self._table[index] == key:
                return
            index = (index + 1) % self._size
            if index == original_index:
                raise RuntimeError("Hash table is full")

        self._table[index] = key

    def __str__(self) -> str:
        result = ""
        for index, key in enumerate(self._table):
            result += f"{index}: {key}\n"
        return result


class HashTableSeparateChaining:
    """Хеш-таблица с разделением цепочек (Со списками)."""

    def __init__(self, size: int) -> None:
        self._size = size
        self._table = [[] for _ in range(size)]

    def insert(self, key: str) -> None:
        index = djb2_hash(key) % self._size
        if key not in self._table[index]:
            self._table[index].append(key)

    def __str__(self) -> str:
        result = ""
        for index, chain in enumerate(self._table):
            chain_string = " -> ".join(chain) if chain else "None"
            result += f"{index}: {chain_string}\n"
        return result


def prepare_text(text: str) -> list[str]:
    # Удаление пунктуации
    for char in string.punctuation:
        text = text.replace(char, "")
    text = text.lower()

    return text.split()


def main() -> None:
    input_file = Path("data/13/input.txt")
    output_file_oa = Path("data/13/output_oa.txt")
    output_file_sc = Path("data/13/output_sc.txt")
    table_size = 89  # Простое число для лучшего распределения

    with open(input_file) as fp:
        text = fp.read()
    words = prepare_text(text)

    hash_table_oa = HashTableOpenAddressing(table_size)
    hash_table_sc = HashTableSeparateChaining(table_size)

    for word in words:
        hash_table_oa.insert(word)
        hash_table_sc.insert(word)

    with open(output_file_oa, "w", encoding="utf-8") as fp:
        fp.write(str(hash_table_oa))

    with open(output_file_sc, "w", encoding="utf-8") as fp:
        fp.write(str(hash_table_sc))

    print("Готово!")


if __name__ == "__main__":
    main()
