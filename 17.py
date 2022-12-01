
def sorting(sequence):
    if len(sequence) < 2:  # если чисел 2,
        return sequence[:]  # выходим из рекурсии
    else:
        middle = len(sequence) // 2  # ищем середину
        left = sorting(sequence[:middle])  # рекурсивно делим левую часть
        right = sorting(sequence[middle:])  # и правую
        return connect(left, right)  # выполняем соединение


def connect(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

sequence = [int(x) for x in input("Введите положительные числа в любом порядке, через пробел: ").split()]

while True:
    try:
        number = int(input("Введите положительное число: "))
        if number < 0:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")
print(f"Отсортированный по возрастанию список: {sorting(sequence)}")
max_index = len(sorting(sequence)) - 1
max_number = sorting(sequence)[-1]
sequence.append(number)
tmp_sorted_sequence = sorting(sequence)
right_border = (len(tmp_sorted_sequence) - 1)
number_index = binary_search(tmp_sorted_sequence, number, 0, right_border)
if number_index == 0:
    print("Введенное число меньше наименьшего числа в списке")
elif number_index - 1 == max_index and number != max_number:
    print('Введенное число больше максимального числа в списке')
else:
    print(f"Позиция искомого числа {number_index - 1}")
    print(f"Искомое число {tmp_sorted_sequence[number_index - 1]}")

