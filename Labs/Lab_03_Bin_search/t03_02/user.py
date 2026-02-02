"""
Реалізуйте інтерфейс для роботи з англійсько-українським словником та швидким пошуком перекладу.
"""

lst = []

def addTranslation(eng, translation):
    """ Додає до словника англійське слово та його переклад.
    Пари (eng, translation) приходяться у порядку, що відповідає лексикографічному порядку.

    :param eng: англійське слово
    :param translation: переклад
    """
    lst.append((eng, translation))


def find(eng):
    """ Повертає переклад слова зі словника.
    :param eng: англійське слово
    :return: переклад слова, якщо воно міститься у словнику, або порожній рядок у іншому разі.
    """
    left = 0
    right = len(lst) - 1

    while left < right:
        mid = left + (right - left) // 2
        #print(f"left: {left}, right: {right}, mid: {mid}")

        if lst[mid][0] < eng:
            left = mid + 1
        else:
            right = mid

    if lst[left][0] == eng:
        return lst[left][1]

    else:
        return ""