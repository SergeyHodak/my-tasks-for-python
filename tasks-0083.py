def replace_last(line: list) -> list:
    """
    В данном списке последний элемент должен стать первым.
    Пустой список или список только с одним элементом должны оставаться неизменными.
    """
    if len(line) < 2:  # список из одного элемента или вообще пустой
        return line  # вернуть как есть
    else:  # в списке два и более элементов
        return line[-1:] + line[:-1]  # отдать, последний спереди стал


if __name__ == '__main__':
    print("Пример:")
    print(replace_last([2, 3, 4, 1]))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")