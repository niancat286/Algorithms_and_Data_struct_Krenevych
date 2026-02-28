import sys


def sort_insertion(array):

    n = len(array)

    for i in range(1, n):
        student = array[i]
        x = (student['cls_num'], student['cls_letter'], student['last_name'])
        j = i - 1

        while j >= 0:
            curr_x = (array[j]['cls_num'], array[j]['cls_letter'], array[j]['last_name'])

            if curr_x > x:
                array[j + 1] = array[j]
                j -= 1
            else:
                break

        array[j + 1] = student


def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    students = []

    idx = 1
    for _ in range(n):
        last_name = input_data[idx]
        first_name = input_data[idx + 1]
        cls_str = input_data[idx + 2]
        dob = input_data[idx + 3]
        idx += 4

        cls_num = int(cls_str[:-1])
        cls_letter = cls_str[-1]

        students.append({
            'last_name': last_name,
            'first_name': first_name,
            'cls_str': cls_str,
            'birth_date': dob,
            'cls_num': cls_num,
            'cls_letter': cls_letter
        })

    sort_insertion(students)

    for s in students:
        print(f"{s['cls_str']} {s['last_name']} {s['first_name']} {s['birth_date']}")


if __name__ == '__main__':
    solution()