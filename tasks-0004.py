def number_length(a: str) -> str:
    """
    Вам дано положительное целое число. Определите сколько цифр оно имеет.
    """
    return len(str(a))


if __name__ == '__main__':
    print("Пример:")
    print(number_length(10))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
