def split_list(items: list) -> list:
    """
    Вы должны разделить данный массив на два массива. Если в нем нечетное
    количество элементов, то первый массив должен иметь больше элементов. Если
    в нем нет элементов, следует вернуть два пустых массива.
    """
    if len(items) == 0:  # если на входе пусто
        return list([[], []])  # вернем пустые массивы
    elif len(items) % 2 == 0:  # если парное количество элементов в массиве
        return list([items[0:int(len(items)/2)], items[int(len(items)/2):]])  # массив ровно пополам
    elif len(items) == 1:  # если количество элементов в массиве = 1
        return list([items, []])  # вернем в первом масиве весеь вход а второй пустой
    else:  # если масив состоит с непаного количества элементов в нем
        return list([items[0:int(len(items)/2)+1], items[int(len(items)/2+1):]])  # в первом на один больше


if __name__ == '__main__':
    print("Пример:")
    print(split_list([]))
    print(split_list([1, 2, 3, 4, 5, 6]))
    print(split_list([1]))
    print(split_list([1, 2, 3]))

    # Эти "assert" используются для самопроверки, а не для автоматического тестирования.
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")