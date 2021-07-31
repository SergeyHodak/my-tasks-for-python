def first_word(text: str) -> str:
    """
    Дана строка и нужно найти ее первое слово.
    - Строка состоит только из английских символов и пробелов.
    - В начале и в конце строки пробелов нет.
    """
    return text.split()[0]


if __name__ == '__main__':
    print("Пример:")
    print(first_word("Hello world"))

    # Эти «asserts» используются для самопроверки, а не для автоматического тестирования.
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить крутые награды!")