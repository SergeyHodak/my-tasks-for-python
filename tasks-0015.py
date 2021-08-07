def correct_sentence(text: str) -> str:
    """
    На вход Вашей функции будет передано одно предложение. Необходимо вернуть
    его исправленную копию так, чтобы оно всегда начиналось с большой буквы и
    заканчивалось точкой.
    Обратите внимание на то, что не все исправления необходимы.
    Если предложение уже заканчивается на точку, то добавлять еще одну не
    нужно, это будет ошибкой
    """
    if text[-1] != ".":  # если в конце нет точки
        text += "."  # приклеять точку
    return text[0].upper() + text[1::]  # выдать повышенный регистр первого символа и все остальное
    

if __name__ == '__main__':
    print("Пример:")
    print(correct_sentence("greetings, friends"))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
