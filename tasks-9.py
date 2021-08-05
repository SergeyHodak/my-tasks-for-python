from typing import Iterable


def replace_first(items: list) -> Iterable:
    """
    В данном списке первый элемент должен стать последним.
    Пустой список или список из одного элемента не должен измениться.
    """
    a = len(items) 
    if a == 0: #если строка пустая
        return items #отдаст как есть
    else: #если строка не пустая
        i=0 #старт с первой позиции тоесть 0
        tmp = items[0] #сохранить первый
        n = len(items) #количество проходов цикла
        for i in range(0, n-1): #для i в диапазоне от 0 до len(A)-1
            items[i] = items[i+1] #записывает в 0 значение из 1, потом в 1 из 2, в 2 из 3
        items[-1] = tmp #выгрузить в последний первый
        return items #отдаст измененную строку

if __name__ == '__main__':
    print("Пример:")
    print(list(replace_first([1, 2, 3, 4])))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
