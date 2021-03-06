"""
    Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву
    в тексте. Результатом должна быть буква в нижнем регистре. При поиске самой частой буквы, регистр не имеет
    значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и
    пробелы, а только буквы. Если в тексте две и больше буквы с одинаковой частотой , тогда результатом будет буква,
    которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
"""
def checkio(text: str) -> str:
    for i in " 0123456789!?`-,":  # пробежка удаляя символы
        text = text.replace(i, "")  # заменяем на пустоту (удаляем)
    text = text.lower()  # сделать нижнего регистра
    a = {}  # пустой словарь
    for i in range(0, len(text)):  # пробежка по символам
        a[text[i]] = text.count(text[i])  # добавить в словарь (ключ, значение)
    b = sorted(a.values())  # вытащить все значения из словаря и отсортировать их на возростание
    if b.count(b[-1]) == 1:  # если такое количество повторений у символа только одно
        for k, v in a.items():  # конструкция цикла для выдачи ключа по значению
            if v == b[-1]:  # если значение в этом ключе рано искомому
                return k  # выдать результат
    else:  # такой символ не один
        c = ""  # пустая строка
        for k, v in a.items():  # конструкция цикла для выдачи ключа по значению
            if v == b[-1]:  # если значение в этом ключе рано искомому
                c = str(c)+str(k)  # записать ключ
        c = sorted(c)  # сортировка по алфавиту
        return c[0]  # выдать первую букву


if __name__ == '__main__':
    print("Пример:")
    print(checkio("Hello World!"))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Начать долгий тест")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("Проведены локальные тесты.")