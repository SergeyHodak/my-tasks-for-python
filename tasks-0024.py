def backward_string_by_word(text: str) -> str:
    """
    В заданной строке вы должны перевернуть каждое слово,
    но слова должны оставаться на своих местах.
    """
    if len(text) == 0:  # если на входе пусто
        return text  # выдать то что было на входе
    a = text.split(" ")  # поделить на слова по пробелам
    b = str()  # пустая строка для выдачи результата
    for i in a:  # пробежка по списку слов
        b += i[::-1] + " "  # записать слово в обратной последовательности букв
    return b[:-1]  # выдать без последнего символа


if __name__ == '__main__':
    print("Пример:")
    print(backward_string_by_word(''))
    print(backward_string_by_word('world'))
    print(backward_string_by_word('hello world'))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
