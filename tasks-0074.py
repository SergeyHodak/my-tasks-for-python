def isometric_strings(a, b):
    """
    Вам надо проверить, что 2 данные строки изометричны. Это значит что символ
    из одной строки может стать в соответствие символам из другой строки.
    Один символ одной строки может соответствовать только одному символу
    другой строки. Два или более символа одной строки могут соответствовать
    одному символу другой строки, но не наоборот.
    """
    def forma(x: str):  # анализ аргумента
        e = str()  # пустая строка
        for i in range(0, len(x)):  # пробежка по первому аргументу
            if i+1 != len(x) and x[i] == x[i+1]:  # если это не последний и ин равен следующему
                e += '1' + str(x.count(x[i]))  # записываем единичку + повторения даной позиции в аргументе
            else:  # если это последний или он не равен следующему
                if i+1 == len(x):  # если последний
                    if x[i-1] == x[i]:  # если последний равен предпоследнему
                        e += '1' + str(x.count(x[i]))  # записываем единичку + повторения даной позиции в аргументе
                    else:  # не равен
                        e += '0' + str(x.count(x[i]))  # записываем нолик + повторения даной позиции в аргументе
                else:  # не последний и не равен следующему
                    e += '0' + str(x.count(x[i]))  # записываем нолик + повторения даной позиции в аргументе
        return e

    if len(a) == 0 and len(b) == 0:  # если аргументы пустые
        return True  # все супер
    c = forma(a)  # строка проанализированная по первому аргументу
    d = forma(b)  # строка проанализированная по второму аргументу
    if c == d:  # если сравниваются
        if len(c) == c.count("0") and len(d) == d.count("0"):  # если везде только нолики
            return False  # фигня
        else:  # наверное присутствуют и единички
            return True  # все супер
    else:  # если не сравниваются
        return False  # фигня


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))  # True
    print(isometric_strings('gogopy', 'doodle'))  # False
    print(isometric_strings("paper", "words"))  # False
    print(isometric_strings('', ''))  # True
    print(isometric_strings("paper", "title"))  # True

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    assert isometric_strings('gogopy', 'doodle') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")