from typing import Iterable


def replace_first(items: list) -> Iterable:
    """
    В данном списке первый элемент должен стать последним.
    Пустой список или список из одного элемента не должен измениться.
    """
    if len(items) == 0:  # если список пустой
        return items  # возврат без изменений
    if len(items) == 1:  # если список только с одного элемента
        return items  # возврат без изменений
    a = items[1:]  # записываем сюда от второго до конца
    a.append(items[0])  # добавим в конец первый символ
    return a  # выдать результат


if __name__ == '__main__':
    print("Пример:")
    print(list(replace_first([1, 2, 3, 4])))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
