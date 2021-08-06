def backward_string(val: str) -> str:
    """
    Вы должны вернуть данную строку в обратном порядке.
    """
    return val[::-1]


if __name__ == '__main__':
    print("Пример:")
    print(backward_string('val'))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
