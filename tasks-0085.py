def is_majority(items: list) -> bool:
    """
    У нас есть список логических значений. Проверим, верны ли большинство элементов.
    Некоторые случаи, о которых стоит упомянуть:
        1) пустой список должен возвращать false;
        2) если истинность и ложь равны, функция должна возвращать ложь.
    """
    a = items.count(True)  # количество повторений истины
    b = items.count(False)  # количество повторений лжи
    if a == b:  # если количество повторений равная
        return False  # лож
    elif a > b:  # если истинны больше чем лжи
        return True  # истина
    else:  # остальные случаи должны быть что лжи больше чем истины
        return False  # лож

if __name__ == '__main__':
    print("Пример:")
    print(is_majority([True, True, False, True, False]))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")