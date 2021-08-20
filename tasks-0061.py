def words_order(text: str, words: list) -> bool:
    """
    У вас есть текст и список слов. Вам нужно проверить, появляются ли слова в списке в том же порядке,
    что и в данном тексте. Случаев, которых следует ожидать при решении этой задачи:
    -    слова из списка нет в тексте - ваша функция должна вернуть False;
    -    любое слово может встречаться в тексте более одного раза - используйте только первое;
    -    два слова в данном списке совпадают - ваша функция должна возвращать False;
    -    условие чувствительно к регистру, что означает, что «привет» и «Привет» - два разных слова;
    -   текст состоит только из английских букв и пробелов.
    Вход: два аргумента. Первый - заданный текст, второй - список слов.
    """
    for i in range(0, len(words)):  # пробежка по словам
        if words.count(words[i]) > 1:  # если это слово встречается больше раза в условиях
            return False  # выдать фальш
    b = text.split()  # поделить текст на список слов по пробелу
    for i in range(0, len(words)):  # пробежка, по словам в поиках их в тексте
        if words[i] not in b:  # если этого слова нет в тексте
            return False  # выдать фальш
    a = []  # пустой список, для создания порядка слов
    for i in range(0, len(words)):  # пробежка по тексту из слов = b, len(words) раз
        a.append(b.index(words[i]))  # записать индекс первого слова находящегося в списке "b"
    if a == sorted(a):  # если после сортировки списки равны
        return True  # вернуть истину
    else:  # если после сортировки списки разные
        return False  # выдать фальш


if __name__ == '__main__':
    print("Пример:")
    print(words_order('hi world im here', ['world', 'world']))  # фальш, два одинаковых в списке слов
    print(words_order('hi world im here', ['country', 'world']))  # фальш, первого слова нету в заданном тексте
    print(words_order('hi world im here', ['world', 'here']))  # правда
    print(words_order('hi world im here', ['here', 'world']))  # фальш, поочередность не соответствует
    print(words_order('', ['world', 'here']))  # фальш, первого слова нету в заданном тексте
    print(words_order('hi world im here', ['world']))  # правда, стово присутствует в тексте
    print(words_order('hi world im here', ['world', 'here', 'hi']))  # False, не совпадение поочередности

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here', ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', ['world', 'im', 'here']) == True
    assert words_order('hi world im here', ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here', ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")