def between_markers(text: str, begin: str, end: str) -> str:
    """
    Вам дана строка и два маркера (начальный и конечный).
    Вам необходимо найти текст, заключенный между двумя этими маркерами.
    Но есть несколько важных условий:
    +-- Начальный и конечный маркеры всегда разные
    -- Если нет начального маркера, то началом считать начало строки
    -- Если нет конечного маркера, то концом считать конец строки
    -- Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
    -- Если конечный маркер стоит перед начальным, то вернуть пустую строку
    """
    s = 0  # флаг работы цикла вайл
    i = 0  # шагатель
    while s == 0:  # ходим пока не получим флаг
        if begin != end:  # если начальный и конечный маркеры разные
            if begin in text and end in text:  # если первый и второй маркеры присутствуют в проверяемой строке
                for posledn in range(i, len(text)):  # пробежда от начала до конца строки
                    if text[posledn: posledn + len(end)] == end:  # если кусочек с "text" длиной второго маркера равен второму маркеру
                        return ""  # если второой маркер встретился первее первого, просят вернуть пустую строку
                    elif text[posledn: posledn + len(begin)] == begin:  # если кусочек с "text" длиной первого маркера равен первому маркеру
                        break  # продолжит анализ строки далее, прервав этот цикл
            if begin in text:  # если имеется начальный маркер в строке
                for esv in range(i, len(text)):  # пробежка от "i" до конца строки "text"
                    if text[esv: esv+len(begin)] == begin:  # если кусочек с "text" длиной первого маркера равен первому маркеру
                        if end in text:  # если имеется конечный маркер в строке
                            for est in range(esv, len(text)):  # пробежка от "esv" до конца строки "text"
                                if text[est: est+len(end)] == end:  # если кусочек с "text" длиной второго маркера равен второму маркеру
                                    s = 1  # закрыть цикл вайл
                                    return text[esv+len(begin): est]  # вернем "text" от конечного символа первого маркера до первого символа конечного маркера
                        else:  # если нет конечного маркера в строке
                            s = 1  # закрыть цикл вайл
                            return text[esv+len(begin):]  # выдать "text" от первого маркера до конца строки
            else:  # если нет начального маркера в строке
                if end in text:  # если имеется конечный маркер в строке
                    for est in range(i, len(text)): # пробежка от "i" до конца строки "text"
                        if text[est: est+len(end)] == end:  # если кусочек с "text" длиной второго маркера равен второму маркеру
                            s = 1  # закрыть цикл вайл
                            return text[0: est]  # вернем "text" от начала до первого символа конечного маркера
                else:  # если нет конечного маркера в строке
                    s = 1  # закрыть цикл вайл
                    return text  # вернуть не вырезанный текст
        else:  # если начальный и конечный маркеры ОДИНАКОВЫ
            s = 1  # закрыть цикл вайл
            return "ERROR = начальный и конечный маркеры не должны быть одинаковые"  # возвращаем ошибку


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers('No [b]hi', '[b]', '[/b]'))  # 'hi', 'No close'

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
