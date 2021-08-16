"""
    Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву
    в тексте. Результатом должна быть буква в нижнем регистре. При поиске самой частой буквы, регистр не имеет
    значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и
    пробелы, а только буквы. Если в тексте две и больше буквы с одинаковой частотой , тогда результатом будет буква,
    которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
"""
def checkio(text: str) -> str:

    # замените это на решение
    return 'a'

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
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("Проведены локальные тесты.")