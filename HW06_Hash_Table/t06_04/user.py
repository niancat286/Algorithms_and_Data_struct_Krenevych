
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:
    __slots__ = ['author', 'title', 'next']

    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.next = None


size: int = 1000003
slots: list
M = 31


def hash_func(key: str) -> int:
    """ Повертає індекс масиву для заданого рядкового ключа. """
    #return abs(hash(key)) % size

    global M
    h = 0
    for i in range(len(key)):
        h = (h * M + ord(key[i])) % size

    return h


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None] * size


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    h = hash_func(author)
    curr = slots[h]

    while curr is not None:
        if curr.author == author and curr.title == title:
            return
        curr = curr.next

    new_node = Node(author, title)
    new_node.next = slots[h]
    slots[h] = new_node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    h = hash_func(author)
    curr = slots[h]

    while curr is not None:
        if curr.author == author and curr.title == title:
            return True
        curr = curr.next

    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    h = hash_func(author)
    curr = slots[h]
    prev = None

    while curr is not None:
        if curr.author == author and curr.title == title:
            if prev is None:
                slots[h] = curr.next
            else:
                prev.next = curr.next
            return

        prev = curr
        curr = curr.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    h = hash_func(author)
    curr = slots[h]
    books = []

    while curr is not None:
        if curr.author == author:
            books.append(curr.title)
        curr = curr.next

    books.sort()
    return books


if __name__ == '__main__':
    init()

    addBook("Шевченко", "Кобзар")
    addBook("Шевченко", "Гайдамаки")
    addBook("Франко", "Захар Беркут")
    addBook("Шевченко", "Катерина")

    print("Книги Шевченка:", findByAuthor("Шевченко"))
    # ['Гайдамаки', 'Катерина', 'Кобзар']

    print("Чи є 'Кобзар'?:", find("Шевченко", "Кобзар"))  # True
    print("Чи є 'Тіні забутих предків'?:", find("Коцюбинський", "Тіні забутих предків"))  # False

    delete("Шевченко", "Гайдамаки")
    print("Книги Шевченка після видалення:", findByAuthor("Шевченко"))
    # ['Катерина', 'Кобзар']
