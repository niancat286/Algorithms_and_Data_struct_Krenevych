class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self._head: Node | None = None
        self._current: Node | None = None
        self._last: Node | None = None

    def empty(self) -> bool:
        return self._head is None

    def set_first(self):
        self._current = self._head

    def set_last(self):
        self._current = self._last

    def next(self):

        if self.empty() or self._current.next is None:
            raise StopIteration

        self._current = self._current.next

    def prev(self):
        if self.empty() or self._current.prev is None:
            raise StopIteration
        self._current = self._current.prev

    def current(self):
        return self._current.item

    def insert_after(self,item):

        node = Node(item)

        if self.empty():
            self._head = self._current = self._last = node
            return

        node.prev = self._current
        node.next = self._current.next

        if self._current is self._last:
            self._last = node
        else:
            self._current.next.prev = node

        self._current.next = node

    def insert_before(self,item):



        node = Node(item)
        if self.empty():
            self._head = self._last = self._current = node
            return

        node.prev = self._current.prev
        node.next = self._current

        if self._current is self._head:
            self._head = node
        else:
            self._current.prev.next = node

        self._current.prev = node

    def delete(self):
        if self.empty():
            return
        if self._head is self._last:
            self._head = self._current = self._last =self._head.next
            return

        if self._current is self._head:
            self._head = self._current.next
        else:
            self._current.prev.next = self._current.next

        if self._current is self._last:
            self._last = self._current.prev
        else:
            self._current.next.prev = self._current.prev

        if self._current.next is None:
            self._current = self._current.prev
        else:
            self._current = self._current.next




lst: DoubleLinkedList

def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = DoubleLinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return lst.empty()


def set_first():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_first()


def set_last():
    """ Робить останній елемент списку, поточним

    Переставляє поточний елемент на останній елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_last()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    lst.next()

def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    lst.prev()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return lst.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    lst.insert_after(item)


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    lst.insert_before(item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.delete()