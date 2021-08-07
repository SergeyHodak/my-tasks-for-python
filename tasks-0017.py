def sum_numbers(text: str) -> int:
    """
    Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
    Если число является частью слова, то его суммировать не нужно.
    Текст состоит из чисел, пробелом и английского алфавита.
    """
    a = text.split( )  # порубать на части используя пробел
    b = []  # пустой список для хранения запчастей из циферных значений
    for i in range(0, len(a)):  # пробежка по словам
        if a[i].isdigit():  # если только цифры
            b.append(int(a[i]))  # записать значение
    return sum(b)  # отдать сумму полученных значений


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas'
                        'painting by Danish artist Anna'
                        'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
