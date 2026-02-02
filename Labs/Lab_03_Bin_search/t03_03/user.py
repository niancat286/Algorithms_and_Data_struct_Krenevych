"""
Реалізуйте алгоритм пошуку номеру найпершого входження до заданого масиву, заданого числа x.
Якщо заданий елемент відсутній у списку - поверніть номер першого елементу, що більший за число x:
                            array[i] >= x
"""


def bsearch_leftmost(array, x):
    """ Бінарний пошук для відшукання найпершого входження заданого числа

    :param array: Відсортований за неспаданням масив цілих чисел
    :param x:     Шукане число
    :return:      Номер шуканого елемента у масиві
    """
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        #print(f"left: {left}, right: {right}, mid: {mid}")

        if array[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left