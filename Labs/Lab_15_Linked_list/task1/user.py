#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self._front = None
        self._curr = None

    def empty(self):
        return self._front is None

    def reset(self):
        self._curr = self._front

    def next(self):
        if self.empty() or self._curr.next is None:
            raise StopIteration

        self._curr = self._curr.next

    def current(self):
        return self._curr.item

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self._curr = self._front = node
            return

        node.next = self._curr.next
        self._curr.next = node




"""
Реалізуйте структуру даних зв'язний (однозв'язний) список з поточним елементом.
"""
lst = LinkedList()

def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst.__init__()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    global lst
    return lst.empty()


def reset():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global lst
    lst.reset()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    global lst
    lst.next()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    global lst
    return lst.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    global lst
    lst.insert_after(item)
