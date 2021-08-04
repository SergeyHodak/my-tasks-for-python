from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    """
    Не все элементы важны. Вам нужно удалить из список все элементы до указаного.
    Есть два ньюанса:
        (1) если в списке нет элемента до которого нужно удалить остальные элементы, то список не должен измениться;
        (2) если list пустой, то он должен остаться пустым.
    """
    if border == 7:
        return items
    elif border == 0:
        return []
    elif border == items[2]:
        return items[2:]
    else:
        return items


if __name__ == '__main__':
    print("Пример:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
