def beginning_zeros(number: str) -> int:
    """
    Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.
    """
    a = str(number)
    k = 0
    b = str(0)
    for i in range(len(a)):
        if a[i] == b:
            k = k+1
        else:
            return k
    return k 
    
if __name__ == '__main__':
    print("Пример:")
    print(beginning_zeros('100'))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
