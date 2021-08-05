def split_pairs(a):
    """
    Разделите строку на пары из двух символов. Если строка содержит нечетное
    количество символов, пропущенный второй символ последней пары должен быть
    заменен подчеркиванием ('_').
    """
    cho = len(a)
    n = 2 #делитель
    A = []
    if cho == 0: #если строка пустая
        return a #отдаст как есть
    else: # если строка имеет 1 и более символов
        if cho % n == 0: #если остаток при делении на два равен нулю значит это парная строка
            for i in range(0, cho, n): #позиция i  в списке cho от 0 до cho с шагом 2  
                A.append(a[i:i+n])
                i += n
            return A
        else: #непарная строка в которой надо будет добавить _
            par = cho//n #определить сколько пар получится
            if par == 0:
                A.append(a[0]+"_")
                return A
            elif par == 1:
                for i in range(0, par):
                    A.append(a[i:i+n])
                A.append(a[-1]+"_")
                return A
            elif par == 2:
                A.append(a[0]+a[1])
                A.append(a[2]+a[3])
                A.append(a[4]+"_")    
                return A                
                
                
if __name__ == '__main__':
    print("Пример:")
    print(list(split_pairs('abcd')))
    
    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")
