import string


def is_acceptable_password(password: str) -> bool:
    """
    В этой миссии вам нужно создать функцию проверки пароля.
    Это условия проверки:
        длина должна быть больше 6;
        должен содержать хотя бы одну цифру, но не может состоять только из цифр;
        наличие цифр или просто цифр не применяется к паролю длиннее 9.
        строка ни в коем случае не должна содержать слова «password»;
        должен содержать 3 разных буквы (или цифры), даже если он длиннее 10
    """

    def dop(password):  # доп функция, уникален ли пароль
        a = []  # пустой список
        for i in range(0, len(password)):  # пробужка по символам введенного пароля
            a += [str(password[i]) + str(
                password.count(password[i]))]  # добавить в список [символ + количество его повторений]
        a = list(set(a))  # удаляет повторения
        if len(a) > 2:  # уникальных символом больше двух
            return True  # все ок
        else:  # уникальных символов мение трех
            return False  # не подходит

    if 10 > len(password) > 6:  # если здесль более шести символов и меньше 10
        if dop(password) and "password" not in password.lower():  # уникален и нет слова "password"
            if len(set(string.digits).intersection(password)) > 0:  # если присутствуют цифры
                if len(set(string.ascii_lowercase).intersection(password.lower())) > 0:  # присутствует строчная буква
                    return True  # все ок есть и цифры и символов 6+
    elif 9 < len(password):  # если пароль длинней чем 9 символов
        if dop(password) and "password" not in password.lower():  # уникален и нет слова "password"
            return True  # все ок
    return False  # выдаем сообщение ото том что это не истинное сообщение пароля


if __name__ == '__main__':
    print("Пример:")
    print(is_acceptable_password('aaaaaa1w'))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")