def is_acceptable_password(password: str) -> bool:
    """
    длина пароля должна быть больше 6.
    """
    return len(password) > 6


if __name__ == '__main__':
    print("Пример:")
    print(is_acceptable_password('short'))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
