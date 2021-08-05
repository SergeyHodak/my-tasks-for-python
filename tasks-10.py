def max_digit(number: int) -> int:
    """
    У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
    """
    a = sorted(str(number))  # превращение числа в строку, и сортировка ее
    return int(a[-1])  # превращение строки в число, и возврат последней цифры


if __name__ == '__main__':
    print("Пример:")
    print(max_digit(0))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
