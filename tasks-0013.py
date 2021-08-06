def nearest_value(values: set, one: int) -> int:
    """
    Найдите ближайшее значение к переданному.
    Вам даны список значений в виде множества (Set) и значение, относительно
    которого, надо найти ближайшее. Например, мы имеем следующий ряд чисел:
    4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9.
    Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7,
    а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.
    Несколько уточнений:
    - Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
    - Ряд чисел всегда не пустой, т.е. размер >= 1;
    - Переданное значение может быть в этом ряде, а значит оно и является ответом;
    - В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
    - Ряд не отсортирован и состоит из уникальных чисел.
    """
    values = sorted(values)
    i = 0
    n = len(values)
    for i in range(0, n):
        if values[0] > one:
            return values[0]
        elif values[i] == one:
            return values[i]
        elif i+1 == n: #если следующий прошод наступит на последнюю сравниваемую
            if values[-1] == one: # если последняя сравниваемая ровна искомой
                return values[-1]
            elif values[-1] < one: #если последняя сравниваемая меньше искомой
                return values[-1]
            else: #есле последний больше чем искомая
                left = one - values[i]
                right = values[i + 1] - one
                if left == right:
                    return values[i]
                elif right < left:
                    return values[i + 1]
                else:
                    return values[i]
        elif values[i] < one:
            if values[i+1] == one:
                return values[i+1]
            elif values[i+1] > one:
                left = one - values[i]
                right = values[i+1] - one
                if left == right:
                    return values[i]
                elif right < left:
                    return values[i+1]
                else:
                    return values[i]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value([4, 7, 10, 11, 12, 17], 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
