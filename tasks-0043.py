"""
    "hieeelalaooo" == "hello"
    Птичка меняет слова по следующим правилам:
    - после каждой согласной буквы она добавляет случайную гласную букву "l" == "la" or "le";
    - после каждой гласной буквы она добавляет две таких же буквы "a" == "aaa";
    - Гласные буквы == "aeiouy".
    - (каждая пара слов разделена одним пробелом).
    - Все слова даны в нижнем регистре.
"""
def translate(text: str) -> str:
    a = 0  # шагатель
    b = ""  # строка на вывод
    while a < len(text):  # пока шагатель меньше количества элементов в тексте
        if text[a] in 'bcdfghjklmnpqrstvwxz':  # если в позиции буквы из списка
            b += text[a]  # запись буквы
            a += 2  # повысить счетчик
        elif text[a] == " ":  # если в позиции пробел
            b += text[a]  # запись пробела
            a += 1  # повысить счетчик
        elif text[a] in "aeiouy":  # если в позиции буквы из списка
            b += text[a]  # запись буквы
            a += 3  # повысить счетчик
    return b  # выдать результат


if __name__ == "__main__":
    print("Пример:")
    print(translate("hieeelalaooo"))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")