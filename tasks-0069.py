def is_all_upper(text: str) -> bool:
    """
    Проверьте, все ли символы в данной строке написаны заглавными буквами.
    Если строка пуста или в ней нет букв - функция должна вернуть False.
    """
    import string
    text = text.replace(' ', '')  # удалить все пробелы
    if len(text) != 0:  # если строка не пуста
        if len(set(string.ascii_lowercase).intersection(text.lower())) > 0:  # присутствует строчная буква
            if text.upper() == text:  # если принудительное повышение регистра не отличается от орыгинала
                return True  # истина
    return False  # фальшонуть


if __name__ == '__main__':
    print("Пример:")
    print(is_all_upper('   '))  # False
    print(is_all_upper('DIGITS123'))  # True
    print(is_all_upper('123'))  # False

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")

    ''' мое первое рашение этой задачи
    # почистить от пробелов и цифр
    text = text.replace(' ', '')  # удалить все пробелы
    if len(text) == 0:  # если полученные данные == пустота
        return False  # фигня дело
    a = str()  # пустая строка
    for i in range(0, len(text)):  # пробежимся по строке без пробелов
        if text[i] not in '0123456789':  # если нет цифры
            a += str(text[i])  # добавить этот символ
    if len(a) == 0:  # если полученные данные == пустота
        return False  # фигня дело
    for i in range(0, len(a)):  # пробежимся по строке без пробелов и цифр
        if a[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  # если нет больших букв
            return False  # фигня дело
    return True  # все ок
    '''