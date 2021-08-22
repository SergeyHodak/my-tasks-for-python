from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    """
    Определите, возрастает ли последовательность элементов items таким образом,
    что каждый из ее элементов строго больше (а не просто равен) предыдущему элементу.
    """
    if len(items) < 2:  # если значений ноль или одно
        return True  # все ок
    for i in range(0, len(items)):  # пробежка по весам выражающихся в цифрах
        if i + 1 != len(items) and items[i] < items[
            i + 1]:  # это не последнее значение списка и предыдущий меньше следующего
            pass  # пропускаем
        else:  # либо последнее значение. либо предыдужий больше следующего
            if i + 1 == len(items):  # последнее значение в списке
                return True  # это последнее значение, значит все супер
            else:  # это не последнее значение, а значит не соответвие старшенству
                return False  # фигня дело


if __name__ == '__main__':
    print("Пример:")
    print(is_ascending([-5, 10, 99, 123456]))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")