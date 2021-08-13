"""
    В данном слове нужно проверить, идет ли один символ только сразу за другим.
    Случаев, которых следует ожидать при решении этой задачи:
    + один из символов отсутствует в данном слове - ваша функция должна вернуть False;
    + любой символ встречается в слове более одного раза - используйте только первый;
    + два символа совпадают - ваша функция должна возвращать False;
    - условие чувствительно к регистру, что означает, что «a» и «A» - два разных символа.
    Вход, три аргумента:
    - первый - это заданная строка;
    - второй - это символ, который должен идти первым;
    - третий - это символ, который должен идти после первого.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word:  # если начального или конечного нету в слове
        return False  # выдать фальш
    if first == second:  # если эти символы равны между собой
        return False  # выдать фальш
    if word.index(second) - word.index(first) == 1:  # если разница позиций первого и второго искомых символов = 1
        return True  # выдать истину
    return False  # выдать фальш


if __name__ == '__main__':
    print("Пример:")
    print(goes_after('world', 'w', 'o'))  # True
    print(goes_after("almaz", "m", "a"))  # False

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")