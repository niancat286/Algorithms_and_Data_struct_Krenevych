
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

size: int = 1000003
slots: list


EMPTY = None
DELETED = "DELETED"
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
    slots = [EMPTY for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    h = hash_func(author)
    first_deleted = -1

    while slots[h] is not EMPTY:
        if slots[h] == DELETED:
            if first_deleted == -1:
                first_deleted = h
        elif slots[h][0] == author and slots[h][1] == title:
            return

        h = (h + 1) % size

    insert_idx = first_deleted if first_deleted != -1 else h
    slots[insert_idx] = (author, title)


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    h = hash_func(author)

    while slots[h] is not EMPTY:
        if slots[h] != DELETED and slots[h][0] == author and slots[h][1] == title:
            return True
        h = (h + 1) % size

    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    h = hash_func(author)

    while slots[h] is not EMPTY:
        if slots[h] != DELETED and slots[h][0] == author and slots[h][1] == title:
            slots[h] = DELETED
            return
        h = (h + 1) % size


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    h = hash_func(author)
    books = []

    while slots[h] is not EMPTY:
        # Якщо комірка не видалена і автор збігається — додаємо книгу до списку
        if slots[h] != DELETED and slots[h][0] == author:
            books.append(slots[h][1])
        h = (h + 1) % size

    return sorted(books)


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
