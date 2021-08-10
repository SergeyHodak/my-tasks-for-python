def backward_string_by_word(text: str) -> str:
    """
    В заданной строке вы должны перевернуть каждое слово,
    но слова должны оставаться на своих местах.
    """
    a = ("")  # строка для вывода изначально пустая
    b = ("")  # строка для временного хранения символов которые будем переворачивать
    i = 0  # шагатель
    while i < len(text):  # пока шагатель меньше количества символов в полученной строке, выполним код
        if text[i] != " ":  # если эта позиция не содержит пробел
            if i == len(text)-1:  # если позиция последняя в строке
                b += text[i]  # прибавить содержимое позиции к переворачиваемой строке
                return a + b[::-1]  # вывернуть содержимое 'b' и прибавить к 'a' отдать этот результат
            else:  # эта позиция не последняя в строке
                b += text[i]  # добавить эту позицию к переворачиваемой строке
                i += 1  # увеличение шагателя на шаг в перед
        else:  # имеется пробел в позиции
            a += b[::-1] + text[i]  # добавим эту позицию к выводимой строке
            b = ("")  # обнулить переворачиваемую строку
            i += 1  # увеличение шагателя на шаг в перед
    return a  # отдать результат


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
