def first_word(text: str) -> str:
    """
    Дана строка и нужно найти ее первое слово.
    При решении задачи обратите внимание на следующие моменты:
    - В строке могут встречатся точки и запятые
    - Строка может начинаться с буквы или, к примеру, с пробела или точки
    - В слове может быть апостроф и он является частью слова
    - Весь текст может быть представлен только одним словом и все
    """
    a = text.split()  # Розбиваем строку на слова по пробелу
    for i in a:  # пробежка по списку полученных фрагментов
        if "." in i:  # если точка в фрагменте
            b = i.split(".")  # Розбиваем строку на слова по точке
            for j in b:  # пробежка по поделенным словам
                if j.isalpha():  # если тут только буквы
                    return j  # выдать фрагмент
        elif "'" in i:  # если есть апостроф в фрагменте
            if "," in i:  # если есть запятая
                return i[:-1]  # відать фрагмент без крайнего символа(запятой)
            return i  # выдать фрагмент
        elif "," in i:  # если есть запятая
            return i[:-1]  # відать фрагмент без крайнего символа(запятой)
        elif i.isalpha():  # если тут только буквы
            return i  # выдать фрагмент


if __name__ == '__main__':
    print("Пример:")
    print(first_word("Hello world"))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")