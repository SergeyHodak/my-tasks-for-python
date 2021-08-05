def max_digit(number: int) -> int:
    """
    У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
    """
    a = number
    m = a%10
    a = a//10
    while a > 0:
        if a%10 > m:
            m = a%10
        a = a//10
    return m


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
