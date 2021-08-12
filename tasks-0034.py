from typing import List, Any  # что-то типа можно в любом типе с ним обращатся и не будет ошибок


def all_the_same(elements: List[Any]) -> bool:
    """
    В этой миссии Вам надо определить, все ли элементы массива равны.
    """
    if len(elements) < 2:  # если тут менее двух элементов
        return True  # выдать истину
    else:  # более одного элемента, нужно проверять
        for i in range(0, len(elements)):  # пробежка
            if elements[0] != elements[i]:  # если первый элемент не равен любому другому
                return False  # выдать фальш
    return True  # выдать истину


if __name__ == '__main__':
    print("Пример:")
    print(all_the_same([1, 1, 1]))

    # Эти "assert" используются для самопроверки, а не для автоматического тестирования.
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")