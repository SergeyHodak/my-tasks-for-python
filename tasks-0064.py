import string


def is_acceptable_password(password: str) -> bool:
    """
    В этой миссии вам необходимо создать функцию проверки пароля.
    Это условия проверки:
        длина должна быть больше 6;
        должен содержать хотя бы одну цифру.
    """
    if len(password) > 6:  # если здесль шесть или более символов
        if len(set(string.digits).intersection(password)) > 0:  # если присутствуют цифры
            return True  # выдать истину (цифры присутствуют и более 6 знаков пароля)
    return False  # выдаем сообщение лож/фальш (пароль короткий) или нет цифр в пароле


if __name__ == '__main__':
    print("Пример:")
    print(is_acceptable_password('short'))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")