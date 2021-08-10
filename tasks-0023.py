def count_digits(text: str) -> int:
    """Вам нужно посчитать количество цифр в данной строке."""
    c = 0  # счетчик цифр
    for i in text:  # пробежка по тексту
        if i in '0123456789/':  # если встретится цифра
            c += 1  # если обнаружена цифра, добавляем единичку в счетчик и шагаем дальше
    return c  # отдаем насчитанный результат


if __name__ == '__main__':
    print("Пример:")
    print(count_digits('hi'))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas'
                        'painting by Danish artist Anna'
                        'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
