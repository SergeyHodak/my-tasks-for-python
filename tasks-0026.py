def between_markers(text: str, begin: str, end: str) -> str:
    """
    Вам дана строка и два маркера (начальный и конечный).
    Вам необходимо найти текст, заключенный между двумя этими маркерами.
    Но есть несколько важных условий:
    - Начальный и конечный маркеры всегда разные
    - Если нет начального маркера, то началом считать начало строки
    - Если нет конечного маркера, то концом считать конец строки
    - Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
    - Если конечный маркер стоит перед начальным, то вернуть пустую строку
    """
    if begin not in text and end not in text:  # если нет ни того ни другого маркера в тексте
        return text  # выдать текст без изменений
    elif begin not in text:  # если нет стартового маркера в тексте
        return text[:text.find(end)]  # выдать от начала до индекса конечного маркера
    elif end not in text:  # если нет конечного маркера в тексте
        return text[text.find(begin) + len(begin):]  # выдать от конечного индекса стар маркера до конца
    else:  # если все супер
        return text[text.find(begin) + len(begin):text.find(end)]  # от начала до конца между маркерами


if __name__ == '__main__':
    print('Пример:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers('No [b]hi', '[b]', '[/b]'))  # 'hi', 'No close'

    # Эти "asserts" используются для самопроверки, а не для тестирования.
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Вау, у тебя все хорошо. Пора это проверить!')
