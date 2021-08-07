def first_word(text: str) -> str:
    """
    Дана строка и нужно найти ее первое слово.
    При решении задачи обратите внимание на следующие моменты:
    В строке могут встречатся точки и запятые
    Строка может начинаться с буквы или, к примеру, с пробела или точки
    В слове может быть апостроф и он является частью слова
    Весь текст может быть представлен только одним словом и все
    """
    a = text.split( )  # Розбиваем строку на слова по раздилителю (пробел)
    b = str(a[0])  # берем первое образовавшеесь слово
    if b[-1] == ",":  # если в этом первом слове есть запятая
        b = b[0:-1]  # отсечем запятую
    elif "." in b:  # если есть точка в первом слове
        for i in range(len(a)):  # цикл от 0 до макс слов в переменной а
            if "." in a[i][0]:  # если есть точка в слове первым символом
                pass  # то есть перейдем на следующее слово
            else:  # здесь точка может быть не в начале слова
                if "." in a[i]:  # точка в слове присутствует
                    c = a[i].split(".")# точка есть поделю по ней на слова и выведу первое
                    return c[0]  # вернем полученный результат
                else:  # все же здесь точки уже нет можем завершить роботу
                    return str(a[i])  # вернем полученный результат
    return b  # вернем полученный результат


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
