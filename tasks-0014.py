def between_markers(text: str, begin: str, end: str) -> str:
    """
    Вам дана строка и два маркера (начальный и конечный). Вам необходимо
    найти текст, заключенный между двумя этими маркерами.
    Но есть несколько важных условий:
    - Начальный и конечный маркеры всегда разные.
    - Начальный и конечный маркеры всегда размером в один символ.
    - Начальный и конечный маркеры всегда есть в строке и идут один за другим.
    """
    n = len(text) #узнал количество символов в строке для проходности
    j = 0
    for i in range(0, n): #идем с шагом и, в строке от нуля до ее конца
        f = i #счетчик символов до закрывающего символа
        if text[i] == begin: #если это символ равен стартовому
            for i in range(i, n):
                if text[i] != end:
                    j = j+1
                    if text[i + 1] == end:  # если следующий символ закрывающий
                        return text[f+1:f+j]
            return text[f+1:f+j]

if __name__ == '__main__':
    print('Пример:')
    print(between_markers('What is >apple<', '>', '<'))

    # Эти "asserts" используются для самопроверки, а не для тестирования.
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Вау, у тебя все хорошо. Пора это проверить!')
