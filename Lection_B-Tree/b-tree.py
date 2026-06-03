class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def print_tree(self, x, l=0):
        print("level", l, " ", "len =", len(x.keys), end=": ")
        for i in x.keys:
            print(i[0], end=" ")
        print()
        if not x.leaf:
            for i in x.child:
                self.print_tree(i, l + 1)

    # Функція пошуку ключа k. Починає з вузла x (за замовчуванням з кореня)
    def search_key(self, k, x=None):
        # Якщо вузол не переданий, починаємо пошук з кореня
        if x is None:
            x = self.root
        i = 0
        # Шукаємо перший ключ у вузлі, який більший або дорівнює шуканому k
        while i < len(x.keys) and k > x.keys[i][0]:
            i += 1

        # Якщо ми знайшли точний збіг ключа у поточному вузлі
        if i < len(x.keys) and k == x.keys[i][0]:
            return (x, i)  # Повертаємо сам вузол та індекс знайденого ключа
        # Якщо ключ не знайдено, і ми знаходимося в листку - значить ключа взагалі немає в дереві
        elif x.leaf:
            return None
        # Інакше (це внутрішній вузол), рекурсивно спускаємося до відповідного нащадка
        else:
            return self.search_key(k, x.child[i])

    # Головна функція вставки ключа
    def insert_key(self, k):
        root = self.root
        # Перевіряємо, чи корінь повністю заповнений (має максимально допустимі 2t-1 ключів)
        if len(root.keys) == (2 * self.t) - 1:
            # Створюємо новий порожній вузол, який стане новим коренем
            temp = BTreeNode()
            self.root = temp
            # Старий корінь стає першим (і єдиним) нащадком нового кореня
            temp.child.insert(0, root)
            # Розщеплюємо старий корінь навпіл. Середній ключ підніметься у новий корінь temp
            self.split(temp, 0)
            # Тепер, коли корінь точно не переповнений, вставляємо ключ
            self.insert_non_full(temp, k)
        else:
            # Якщо корінь не переповнений, просто викликаємо логіку вставки
            self.insert_non_full(root, k)

    # Вставка ключа k у вузол x, про який ми ВЖЕ ЗНАЄМО, що він не переповнений
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1  # Починаємо з останнього індексу ключів

        # Якщо ми дійшли до листка, просто вставляємо ключ у правильне місце
        if x.leaf:
            x.keys.append((None, None))  # Додаємо порожнє місце в кінець масиву
            # Зсуваємо всі ключі, більші за k, на одну позицію вправо
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            # Вставляємо наш ключ на звільнене місце
            x.keys[i + 1] = k
        # Якщо це внутрішній вузол (не листок)
        else:
            # Шукаємо правильного нащадка, в якого треба спуститися
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1  # Індекс нащадка, в якого ми маємо спуститися

            # Якщо цей нащадок вже повністю заповнений
            if len(x.child[i].keys) == (2 * self.t) - 1:
                # Спочатку розщеплюємо його
                self.split(x, i)
                # Після розщеплення середній ключ піднявся у вузол x.
                # Треба перевірити, в яку з двох нових половинок нащадка нам тепер спускатися
                if k[0] > x.keys[i][0]:
                    i += 1
            # Рекурсивно вставляємо ключ у гарантовано не переповненого нащадка
            self.insert_non_full(x.child[i], k)

    # Функція розщеплення повністю заповненого нащадка y (який є i-тою дитиною вузла x)
    def split(self, x, i):
        t = self.t
        y = x.child[i]  # Вузол y, який ми будемо розщеплювати
        z = BTreeNode(y.leaf)  # Створюємо новий вузол z (брата для y)

        # Додаємо новий вузол z у список дітей вузла x
        x.child.insert(i + 1, z)
        # Піднімаємо середній (медіанний) ключ з y у батьківський вузол x
        x.keys.insert(i, y.keys[t - 1])

        # Передаємо вузлу z праву половину ключів вузла y
        z.keys = y.keys[t: (2 * t) - 1]
        # Вузол y залишає собі лише ліву половину ключів
        y.keys = y.keys[0: t - 1]

        # Якщо розщеплюється не листок, треба розділити і дітей
        if not y.leaf:
            # Вузол z забирає праву половину дітей
            z.child = y.child[t: 2 * t]
            # Вузол y залишає собі ліву половину дітей
            y.child = y.child[0: t]

    # ==========================================
    # БЛОК ВИДАЛЕННЯ (DELETION)
    # ==========================================

    # Головна зовнішня функція для видалення ключа
    def delete_key(self, k):
        # Якщо дерево порожнє, нічого робити
        if not self.root.keys:
            print("Дерево порожнє")
            return

        # Викликаємо внутрішню рекурсивну функцію видалення, починаючи з кореня
        self._delete(self.root, k)

        # Спеціальний випадок: якщо після видалення корінь залишився взагалі без ключів...
        if len(self.root.keys) == 0:
            # ...але має дітей, то його перша (і єдина) дитина стає новим коренем (висота дерева зменшується)
            if not self.root.leaf:
                self.root = self.root.child[0]

    # Рекурсивна функція видалення ключа k з піддерева з коренем x
    def _delete(self, x, k):
        # Знаходимо індекс ключа, який більший або дорівнює шуканому k
        idx = self._find_key(x, k)

        # УМОВА 1: Ключ знайдено безпосередньо у поточному вузлі x
        if idx < len(x.keys) and x.keys[idx][0] == k:
            # Якщо це листок - просто видаляємо
            if x.leaf:
                self._remove_from_leaf(x, idx)
            # Якщо це внутрішній вузол - запускаємо складну процедуру заміни
            else:
                self._remove_from_non_leaf(x, idx)

        # УМОВА 2: Ключа в поточному вузлі немає (він має бути нижче в дереві)
        else:
            # Якщо ми вже в листку, а ключа немає - його не існує
            if x.leaf:
                print(f"Ключ {k} не знайдено.")
                return

            # Запам'ятовуємо, чи ми плануємо спускатися в останню (найправішу) дитину
            flag = (idx == len(x.keys))

            # Якщо дитина, в яку ми маємо спуститися, "бідна" (має менше t ключів),
            # ми її превентивно поповнюємо, щоб не зламати дерево при видаленні
            if len(x.child[idx].keys) < self.t:
                self._fill(x, idx)

            # Після функції _fill міг відбутися злив (merge) вузлів.
            # Якщо ми йшли в останню дитину, і вона злилася з попередньою, індекс змістився
            if flag and idx > len(x.keys):
                self._delete(x.child[idx - 1], k)
            else:
                # Нормальний спуск у дитину для продовження пошуку/видалення
                self._delete(x.child[idx], k)

    def _find_key(self, x, k):
        """Знайти індекс першого ключа, який більший або дорівнює k"""
        idx = 0
        while idx < len(x.keys) and x.keys[idx][0] < k:
            idx += 1
        return idx

    def _remove_from_leaf(self, x, idx):
        """Видалити ключ з листового вузла"""
        x.keys.pop(idx)

    def _remove_from_non_leaf(self, x, idx):
        """Видалити ключ із внутрішнього вузла"""
        k = x.keys[idx][0]

        # Випадок 1: Лівий нащадок має достатньо ключів
        if len(x.child[idx].keys) >= self.t:
            pred = self._get_pred(x, idx)
            x.keys[idx] = pred
            self._delete(x.child[idx], pred[0])

        # Випадок 2: Правий нащадок має достатньо ключів
        elif len(x.child[idx + 1].keys) >= self.t:
            succ = self._get_succ(x, idx)
            x.keys[idx] = succ
            self._delete(x.child[idx + 1], succ[0])

        # Випадок 3: Обидва нащадки мають мінімум ключів (t-1). Зливаємо їх
        else:
            self._merge(x, idx)
            self._delete(x.child[idx], k)

    def _get_pred(self, x, idx):
        """Отримати попередника (максимальний ключ у лівому піддереві)"""
        curr = x.child[idx]
        while not curr.leaf:
            curr = curr.child[len(curr.keys)]
        return curr.keys[-1]

    def _get_succ(self, x, idx):
        """Отримати наступника (мінімальний ключ у правому піддереві)"""
        curr = x.child[idx + 1]
        while not curr.leaf:
            curr = curr.child[0]
        return curr.keys[0]

    def _fill(self, x, idx):
        """Поповнити вузол child[idx], якщо в ньому менше ніж t ключів"""
        # Пробуємо позичити зліва
        if idx != 0 and len(x.child[idx - 1].keys) >= self.t:
            self._borrow_from_prev(x, idx)
        # Пробуємо позичити справа
        elif idx != len(x.keys) and len(x.child[idx + 1].keys) >= self.t:
            self._borrow_from_next(x, idx)
        # Якщо ні в кого позичити, зливаємо з братом
        else:
            if idx != len(x.keys):
                self._merge(x, idx)
            else:
                self._merge(x, idx - 1)

    def _borrow_from_prev(self, x, idx):
        child = x.child[idx]
        sibling = x.child[idx - 1]

        child.keys.insert(0, x.keys[idx - 1])
        if not child.leaf:
            child.child.insert(0, sibling.child.pop())

        x.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, x, idx):
        child = x.child[idx]
        sibling = x.child[idx + 1]

        child.keys.append(x.keys[idx])
        if not child.leaf:
            child.child.append(sibling.child.pop(0))

        x.keys[idx] = sibling.keys.pop(0)

    def _merge(self, x, idx):
        child = x.child[idx]
        sibling = x.child[idx + 1]

        # Стягуємо ключ з батька у лівого нащадка
        child.keys.append(x.keys.pop(idx))

        # Переносимо всі ключі та нащадків з правого брата у лівого
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.child.extend(sibling.child)

        # Видаляємо посилання на правого брата, оскільки ми його поглинули
        x.child.pop(idx + 1)


# ==========================================
# ТЕСТУВАННЯ
# ==========================================
def main():
    B = BTree(3)

    # Вставка елементів
    for i in range(10):
        B.insert_key((i, 2 * i))

    print("дерево на початку")
    B.print_tree(B.root)

    print("\nВидалення ключа 4:")
    B.delete_key(4)
    B.print_tree(B.root)

    print("\nВидалення ключа 8:")
    B.delete_key(8)
    B.print_tree(B.root)

    print(B.search_key(9))


if __name__ == '__main__':
    main()