from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    """
    Не все элементы важны. Что вам здесь нужно сделать, так это удалить из
    списка все элементы, следующие за данным.
    пример:
        Для иллюстрации у нас есть список [1, 2, 3, 4, 5], и нам нужно удалить
            все элементы, которые идут после 3, то есть 4 и 5.
        У нас есть два крайних случая: (1) если режущий элемент не может быть
            найден, то список не следует изменять; (2) если список пуст, он
            должен оставаться пустым.
    """
    if border not in items:  # режущий элеент не найден
        return items  # возврет не изменяя
    elif len(items) == 0:  # список пуст
        return items  # возврет не изменяя
    a = []  # пустой список
    for i in range(0, len(items)):  # пробежка по "items"
        if items[i] != border:  # если эти символы не равны друг другу
            a.append(items[i])  # записали этот символ
        else:  # равные
            a.append(items[i])  # отдаем
            return a


if __name__ == '__main__':
    print("Пример:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")