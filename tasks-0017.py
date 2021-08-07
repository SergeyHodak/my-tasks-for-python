def sum_numbers(text: str) -> int:
    # your code here
    '''
    Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом. Если число является частью слова, то его суммировать не нужно.
    Текст состоит из чисел, пробелом и английского алфавита.
    '''
    c = 0
    n = len(text) # количество проверяемых символов
    if n == 0:
        return 0
    if text[0] in '0123456789/':
        c = text[0]
        m = 0
        i = 0
        for i in range(i, n):  # с шагом от i до последнего символа в строке
            if text[i] in '0123456789/':  # если символ равен цифре из списка
                m += 1
                continue  # продолжить с начала
            else:
                break  # выход с цикла
        c = text[0:i+m]
    a = 0
    for i in range(0, n): # с шагом от первого до последнего символа в строке
        f = i
        if text[i] == str(' ') or i == 0:
            if text[i+1] in '0123456789/': # если символ равен цифре из списка
                i = i+1
                e = 0
                for i in range(i, n):  # с шагом от i до последнего символа в строке
                    if text[i] in '0123456789/':  # если символ равен цифре из списка
                        e += 1
                        continue  # продолжить с начала
                    else:
                        break  # выход с цикла
                a = text[f+1:f+1+e]
                if text[i] != str(' '):
                    if i+1 == n:
                        break
                    else:
                        a = 0
                break
    b = 0
    for i in range(i, n): # с шагом от первого до последнего символа в строке
        f = i
        if text[i] == str(' ') or i == 0:
            if text[i+1] in '0123456789/': # если символ равен цифре из списк
                i = i+1
                z = 0
                for i in range(i, n):  # с шагом от i до последнего символа в строке
                    if text[i] in '0123456789/':  # если символ равен цифре из списка
                        z += 1
                        continue  # продолжить с начала
                    else:
                        break  # выход с цикла
                b = text[f+1:f+1+z]
                if text[i] != str(' '):
                    if i+1 == n:
                        break
                    else:
                        b = 0
                break
    return int(a)+int(b)+int(c)


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
