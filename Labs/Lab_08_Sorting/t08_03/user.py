
"""
Реалізуйте алгоритм сортування вибором.
"""

N = 10000    # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.

    n = len(array)
    for j in range(n-1):
        pos = j
        for i in range(j+1, n):
            if array[i] < array[pos]:
                pos = i
        array[pos], array[j] = array[j], array[pos]
        print(array)
    """

    n = len(array)
    for j in range(n-1, 0, -1):
        pos = 0
        for i in range(1, j+1):
            if array[i] > array[pos]:
                pos = i
        array[pos], array[j] = array[j], array[pos]
        print(array)


if __name__ == "__main__":
    array = [-3, 4, 5, -7, 21, 8, 10, 20, 13, -9]
    print(array)
    sort(array)