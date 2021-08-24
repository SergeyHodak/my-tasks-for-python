"""
    Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины.
    В сортированом массиве с нечётным числом элементов медиана — это число в середине массива.
    Для массива с чётным числом элементов, где нет одного элемента точно посередине, медиана — это среднее
    значение двух чисел, находящихся в середине массива. В этой задаче дан непустой массив натуральных чисел.
    Вам необходимо найти медиану данного массива.
"""
from typing import List


def checkio(data: List[int]) -> [int, float]:
    data = sorted(data)  # отсортировать
    if len(data) % 2 == 0:  # четное количество элементов
        return (data[int(len(data)/2)-1] + data[int(len(data)/2)]) / 2  # сумировать два значенияи всередине и /2
    else:  # не четное
        return data[int(len(data)/2)]  # выдать элемнт который по середине списка


# Эти "asserts" используются только для самопроверки и не нужны для автоматического тестирования.
if __name__ == '__main__':
    print("Пример:")
    print(checkio([1, 2, 3, 4, 5, 6]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Отсортированный список"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Несортированный список"
    assert checkio([1, 300, 2, 200, 1]) == 2, "Это не в среднем"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Равномерная длина"
    print("Начать долгий тест")
    assert checkio(list(range(1000000))) == 499999.5, "Длинный."
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")