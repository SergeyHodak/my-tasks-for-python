def beginning_zeros(number: str) -> int:
    """
    Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.
    """
    a = 0  # счетчик нулей
    for i in number:  # посимвольная пробезка по строке
        if i == '0':  # если эта позиция равна нулю
            a += 1  # зафиксировать ноль
        else:  # эта позиция не равна нулю
            break  # прервать цикл
    return a  # выдать результат
    
    
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
