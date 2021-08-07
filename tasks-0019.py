def checkio(words: str) -> bool:
    """Давайте научим наших роботов отличать слова от чисел.
    Дана строка со словами и числами, разделенными пробелами (один пробел между
    словами и/или числами). Слова состоят только из букв. Вам нужно проверить
    есть ли в исходной строке три слова подряд.
    Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
    """
    slovo: list = []  # создадим новую строку
    n = len(words)  # узнаем счетчик беганья
    i = 0  # назначим точку старта
    if " " in words:  # если есть пробел True
        pass  # пропустим ход
    else:  # если нет пробела False
        return False  # то конец проверке, оттадем результат
    for i in range(0, n):  # пробежимся по списку
        if words[i] in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz/': # содержит ли список буквы
            slovo.append(1)  # фиксируем букву
            pass  # идем дальше
        elif words[i] == " ":  # если встретился пробел
            slovo.append(0)  # фиксируем пробел
        elif words[i] in '0123456789/':  # если встретится цифра
            slovo.append(2)  # фиксируем цифру
    if 2 in slovo:  # если присутствует 1 и более цифр в строке
        i = 0  # назначим точку старта
        probel1 = 0  # считаем пробелами
        for i in range(i, n):  # пробежка от нуля до макс по строке
            if slovo[i] == 0:  # если в положении присутствует пробел то ессть нолик
                probel1 = probel1+1  # фиксируем найденный пробел в счетчик
            elif slovo[i] == 2:  # если в положении присутствует цифра то ессть двоечка
                probel1 = probel1-1
                break  # выходим с цикла
        i = i+1
        probel2 = 0
        for i in range(i, n):  # пробежка от нуля до макс по строке
            if slovo[i] == 0:  # если в положении присутствует пробел то ессть нолик
                probel2 = probel2+1  # фиксируем найденный пробел в счетчик
            elif slovo[i] == 2:  # если в положении присутствует цифра то ессть двоечка
                probel2 = probel2 - 1
                break  # выходим с цикла
        i = i+1
        probel3 = 0
        for i in range(i, n):  # пробежка от нуля до макс по строке
            if slovo[i] == 0:  # если в положении присутствует пробел то ессть нолик
                probel3 = probel3+1  # фиксируем найденный пробел в счетчик
            elif slovo[i] == 2:  # если в положении присутствует цифра то ессть двоечка
                probel3 = probel3-1
                break  # выходим с цикла
        if probel1 >= 2:  # если пробелов насчитали два и более
            return True  # пробелов два и более значит слов подряд три и более - мы довольны
        elif probel2 >= 3:  # если пробелов насчитали два и более
            return True  # пробелов два и более значит слов подряд три и более - мы довольны
        elif probel3 >= 3:  # если пробелов насчитали два и более
            return True  # пробелов два и более значит слов подряд три и более - мы довольны
        return False  # пробелов один мы не довольны
    else:  # цифры отсутствуют
        i = 0  # назначим точку старта
        probel = 0  # считаем пробелами
        for i in range(0, n):  # пробежка от нуля до макс по строке
            if slovo[i] == 0:  # если в положении присутствует пробел то ессть нолик
                probel = probel+1  # фиксируем найденный пробел в счетчик
        if probel >= 2:  # если пробелов насчитали два и более
            return True  # пробелов два и более значит слов подряд три и более - мы довольны
        return False  # пробелов один мы не довольны

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"  
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
