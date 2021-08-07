def correct_sentence(text: str) -> str:
    """
    На вход Вашей функции будет передано одно предложение. Необходимо вернуть
    его исправленную копию так, чтобы оно всегда начиналось с большой буквы и
    заканчивалось точкой.
    Обратите внимание на то, что не все исправления необходимы.
    Если предложение уже заканчивается на точку, то добавлять еще одну не
    нужно, это будет ошибкой
    """
    t = text[0].upper()  # повысит регистр
    text = t + text[1:]  # повысит регистр
    if text[-1] == ".":  # если в концее есть точка
        return text
    else:  # если точки нет
        text = text + "."
        return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    print("Coding complete? Click 'Check' to earn cool rewards!")
