def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
        Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
        затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
        Для пустого массива результат всегда 0 (ноль).
    """
    if len(array) == 0:
        return 0
    else:
        a = []
        i = 0
        while i < len(array):
            a.append(array[i])
            i += 2
        return sum(a)*array[-1]
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(checkio([6]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
