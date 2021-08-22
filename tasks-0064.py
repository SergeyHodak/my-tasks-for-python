import string


def is_acceptable_password(password: str) -> bool:
    """
    В этой миссии вам необходимо создать функцию проверки пароля.
    Это условия проверки:
        длина должна быть больше 6;
        должен содержать хотя бы одну цифру.
    """
    if len(password) >= 6:  # если здесль шесть или более символов
        # if text[i] in '0123456789/':  # если символ равен цифре из списка
        if len(set(string.digits).intersection(password)) > 0:  # если присутствуют цифры
            return True  # все ок есть и цифры и символов 6+
        else:  # цифры отсутствуют
            return False  # не подходит
    else:  # символов мение 6
        return False  # выдаем сообщение ото том что это не истинное сообщение пароля


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