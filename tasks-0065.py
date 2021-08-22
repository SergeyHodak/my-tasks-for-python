import string


def is_acceptable_password(password: str) -> bool:
    """
    В этой миссии вам необходимо создать функцию проверки пароля.
    Это условия проверки:
        длина должна быть больше 6;
        должен содержать хотя бы одну цифру, но не может состоять только из цифр.
    """
    if len(password) > 6:  # если здесль более шести символов
        if len(set(string.digits).intersection(password)) >= 1:  # если присутствуют цифры
            if len(set(string.ascii_lowercase).intersection(password)) > 0:  # присутствует строчная буква
                return True  # все ок есть и цифры и символов 6+
            elif len(set(string.ascii_uppercase).intersection(password)) > 0:  # буквы в верхнем регистре
                return True  # все ок есть и цифры и символов 6+
            else:
                return False  # не подходит
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
    assert is_acceptable_password('1234567') == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")