"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з розв’язанням колізій методом ланцюжків.
"""

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node(key = {self.key}, value = {self.value}, next = {self.next}"

size: int = 11
slots: list[None | Node]

def hash(key):
    return key % size

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    h = hash(key)
    node = slots[h]

    while node is not None:
        if node.key == key:
            node.value = value
            return
        node = node.next

    node = Node(key, value)
    node.next = slots[h]
    slots[h] = node


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """

    h = hash(key)
    node = slots[h]
    while node is not None:
        if node.key == key:
            return node.value

        node = node.next
    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    h = hash(key)
    node = slots[h]

    if node is None:
        return

    if node.key == key:
        slots[h] = node.next
        return

    prev = node
    node = node.next

    while node is not None:
        if node.key == key:
            prev.next = node.next
            return
        prev = node
        node = node.next




if __name__ == "__main__":
    init()
    print(slots)

    set(5, "5")
    set(27, "27")

    print(slots)