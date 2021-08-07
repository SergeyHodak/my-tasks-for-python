def is_even(num: int) -> bool:
    """
    Проверить является ли число четным или нет. Ваша функция должна возвращать
    True если число четное, и False если число не четное.
    """
    return num % 2 == 0 # если остаток при дилении на 2 равен 0. значит четное


if __name__ == '__main__':
    print("Пример:")
    print(is_even(2))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
