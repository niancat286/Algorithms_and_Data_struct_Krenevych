import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    R = int(input_data[0])  # Кількість рисових полів
    L = int(input_data[1])  # Максимальна координата
    B = int(input_data[2])  # Наш бюджет у батах

    # Створюємо список координат полів
    fields = []
    for i in range(3, 3 + R):
        fields.append(int(input_data[i]))

    #pref_sums[i] буде зберігати суму перших i полів.
    pref_sums = [0] * (R + 1)   #додаємо зайвий 0 на самий початок, щоб було зручно віднімати і не виходити за межі масиву
    for i in range(R):
        pref_sums[i + 1] = pref_sums[i] + fields[i]

    # Функція видає суму координат полів від індексу `left` до `right`
    def get_sum(left, right):
        return pref_sums[right + 1] - pref_sums[left]

    # "Чи можемо ми доставити рис з k полів, не перевищивши бюджет B?"
    def can_deliver(k):
        # Проходимо "вікном" розміром k по масиву полів
        # start - індекс першого поля у вікні
        for start in range(R - k + 1):
            end = start + k - 1  # індекс останнього поля у вікні

            # Оптимальне місце для хабу — це завжди центральне поле у нашому вікні (медіана)
            mid = (start + end) // 2
            hub_pos = fields[mid]

            # Рахуємо вартість доставки з лівої половини вікна до хабу
            # Формула: (кількість_полів_зліва * координата_хабу) - сума_їх_координат
            left_count = mid - start + 1
            left_sum = get_sum(start, mid)
            cost_left = (left_count * hub_pos) - left_sum

            # Рахуємо вартість доставки з правої половини вікна до хабу
            # Формула: сума_їх_координат - (кількість_полів_справа * координата_хабу)
            right_count = end - mid
            if right_count > 0:
                right_sum = get_sum(mid + 1, end)
                cost_right = right_sum - (right_count * hub_pos)
            else:
                cost_right = 0  # Якщо правої частини немає (наприклад k=1)

            total_cost = cost_left + cost_right

            # Якщо знайшли хоча б одне вікно, де вартість <= бюджету, повертаємо True
            if total_cost <= B:
                return True

        # Якщо перевірили всі можливі вікна і жодне не влізло в бюджет
        return False

    # БІНАРНИЙ ПОШУК ПО ВІДПОВІДІ
    low = 1  # Мінімальна кількість вантажівок (хоча б 1 завжди можна безкоштовно)
    high = R  # Максимальна можлива кількість вантажівок
    best_ans = 1  # Змінна для збереження найкращого результату

    while low <= high:
        # Беремо середину: пробуємо взяти k вантажівок
        mid = low + (high - low) // 2

        # Запитуємо нашу функцію перевірки
        if can_deliver(mid) == True:
            best_ans = mid  # Зберігаємо цей успішний результат
            low = mid + 1  # І йдемо шукати, чи можемо ми взяти ЩЕ БІЛЬШЕ (рухаємо ліву межу)
        else:
            high = mid - 1  # Грошей не вистачило, треба брати МЕНШЕ вантажівок (рухаємо праву межу)

    # Виводимо знайдену максимальну кількість
    print(best_ans)


if __name__ == '__main__':
    solve()