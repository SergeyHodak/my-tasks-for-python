def checkio(data):
    """
    Математически счастливые билеты
    Концепция «Математически счастливых билетов» аналогична идее русских «Счастливых билетов». Это относится к старым
    билетам на общественный транспорт, на которых были напечатаны шестизначные числа.
    Вам дается номер билета, и комбинация его цифр может стать математическим выражением, если следовать этим правилам.
        1. Цифры номера можно разбить на группы цифр.
        2. Вы не можете изменить порядок групп или цифр.
        3. Каждая группа рассматривается как одно целое число. (1 и 2 станут 12 и т. Д.)
        4. Рабочие знаки (+, -, * и /) помещаются между группами.
        5. Подвыражения заключаются в круглые скобки, чтобы исключить двусмысленность.
        в порядке оценки.
    Например:
        * 238756 -> (2 * (38 + ((7 + 5) * 6)))
        * 000859 -> (0 + (00 + (8 + (5 + 9))))
        * 561403 -> (5 * (6 + (1 + (40/3))))
    Билет считается математически удачным, если никакая комбинация его цифр не дает значения 100. Например:
        * 000000, очевидно, везет, независимо от того, какую комбинацию вы создаете, всегда
        оценивается в ноль,
        * 707409 и 561709 тоже удачливы, потому что они не могут оценить до 100
        * 595347 не повезло: (5 + ((9 * 5) + (3 + 47))) = 100
        * 593347 не повезло: (5 + ((9 / (3/34)) - 7)) = 100
        * 271353 не повезло: (2 - (7 * (((1/3) - 5) * 3))) = 100
    Комбинация должна быть оценена до 100, чтобы считаться неудачной. Дроби могут встречаться в промежуточных вычислениях (как в приведенных выше примерах для 593347 и 271353), но результат должен быть целым числом.
    Задача: по 6-значному номеру билета программа должна определить, является ли билет математически удачным или нет.
    Ввод: 6 цифр в виде строки.
    Вывод: математически это удачно или нет в виде логического значения.
    Пример:
    checkio ('000000') == Истина
    checkio ('707409') == Верно
    checkio ('595347') == Ложь
    checkio ('271353') == Ложь
    Как это используется: Это хорошая игра для улучшения умственных расчетов. Если у вас есть друзья-программисты или математики, то вы можете дать им это как вызов. Какой код будет проверять цифры быстрее, чем другие? После решения этой задачи у вас появятся навыки жульничества! ;-)
    Предварительное условие: | цифры | == 6
    """

    def divide(data):  # подпрога, генирирующая математические формулы под номер билета, и выдавая ответ на эту формулу
        # как целое число (допускается более 10)
        yield int(data)  # уберает нолики перед (так же отправляет результат для проверки вызывающему эту под функцию)

        # делить 123456: 1 23456, 12 3456, 123 456, ...
        for pos in range(1, len(data)):  # пробежка от 1 до конца цифер, pos - шагатель
            for left in divide(data[:pos]):  # пробежка еще раз вызывая функцию, отдает от начала до pos
                for right in divide(data[pos:]):  # пробежка еще раз вызывая подункцию, отдавая ей от pos до конца цифры
                    # вычислить + - * /
                    yield left + right  # суммирует, (так же отправляет результат для проверки вызывающему эту под функцию)
                    yield left - right  # отнимает, (так же отправляет результат для проверки вызывающему эту под функцию)
                    yield left * right  # перемножает, (так же отправляет результат для проверки вызывающему эту под функцию)
                    if right:  # если есть правая часть
                        yield left / right  # делит, (так же отправляет результат для проверки вызывающему эту под функцию)

    # перечислить все образцы
    for i in divide(data):  # из-за такого обращения тут десятки тысяч шагов проверки
        if i == 100:  # если "i" равна "100"
            return False  # если в кокойто комбинации получили 100 - билет не счастливый
    return True  # билет счастливый, ни одна из комбинаций не дла 100


if __name__ == '__main__':
    print("Пример:")
    # print(checkio('000000'))  # True
    print(checkio('707409'))  # True
    print(checkio('593347'))  # False
    print(checkio('271353'))  # False
    print(checkio('595347'))  # False
    print(checkio('000955'))  # False
    print(checkio('100479'))  # False
    print(checkio('836403'))  # False
    print(checkio('574699'))  # False
    print(checkio('324347'))  # False
    print(checkio('064377'))  # True
    print(checkio('111111'))  # False
    print(checkio('555555'))  # False
    print(checkio('777777'))  # False
    print(checkio('392039'))  # False
    print(checkio('712922'))  # False
    print(checkio('142686'))  # False
    print(checkio('980072'))  # False
    print(checkio('141463'))  # False
    print(checkio('963181'))  # False
    print(checkio('133289'))  # False
    print(checkio('193015'))  # False
    print(checkio('279216'))  # False
    print(checkio('923897'))  # False
    print(checkio('313159'))  # False
    print(checkio('353525'))  # False
    print(checkio('103818'))  # False
    print(checkio('686997'))  # False
    print(checkio('237867'))  # False
    print(checkio('874098'))  # False
    print(checkio('173403'))  # False
    print(checkio('725126'))  # True

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert checkio('000000') == True,  "Все нули"
    assert checkio('707409') == True,  "Вы не можете преобразовать его в 100"
    assert checkio('000955') == False, "(0 + (0 + (0 + (95 + 5)))) = 100"
    assert checkio('712922') == False, "(7 + (1 + (2 + (92 - 2)))) = 100"
    assert checkio('963181') == False, "(9 + (6 + (3 + (1 + 81)))) = 100"
    assert checkio('100479') == False, "(1 + (0 + (0 + ((4 + 7) * 9)))) = 100"
    assert checkio('103818') == False, "(1 + (0 + ((3 + 8) * (1 + 8)))) = 100"
    assert checkio('686997') == False, "(6 + (8 - (6 - (99 - 7)))) = 100"
    assert checkio('279216') == False, "(2 + (7 * (9 - (2 - (1 + 6))))) = 100"
    assert checkio('133289') == False, "(1 + (3 * (32 - (8 - 9)))) = 100"
    assert checkio('193015') == False, "(1 + (93 + (0 + (1 + 5)))) = 100"
    assert checkio('595347') == False, "(5 + ((9 * 5) + (3 + 47))) = 100"
    assert checkio('324347') == False, "(3 + ((2 * 43) + (4 + 7))) = 100"
    assert checkio('677838') == False, "(6 + ((7 * (7 + 8)) - (3 + 8))) = 100"
    assert checkio('141463') == False, "(1 + ((4 * (1 * (4 * 6))) + 3)) = 100"
    assert checkio('555555') == False, "(5 + ((5 * ((5 * 5) - 5)) - 5)) = 100"
    assert checkio('593347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('923897') == False, "(9 + (((2 * (3 + 8)) - 9) * 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
    assert checkio('574699') == False, "(5 - ((7 * (4 - 6)) - (9 * 9))) = 100"
    assert checkio('142686') == False, "(1 * (4 + ((2 + (6 + 8)) * 6))) = 100"
    assert checkio('111111') == False, "(1 * (111 - 11)) = 100"
    assert checkio('980072') == False, "(9 * (800 / 72)) = 100"
    assert checkio('836403') == False, "(8 * ((3 / 6) + (4 * 03))) = 100"
    assert checkio('064377') == True,  "(0 * ((6 / 4) + (3 * 77))) = 100"
    assert checkio('353525') == False, "(3 * ((5 / (3 / 5)) + 25)) = 100"
    assert checkio('237867') == False, "(23 + (78 + (6 - 7))) = 100"
    assert checkio('777777') == False, "((7 + 7) * (7 + (7 / (7 * 7)))) = 100"
    assert checkio('392039') == False, "((3 + 9) * ((2 / (0 - 3)) + 9)) = 100"
    assert checkio('313159') == False, "((3 * (1 + 31)) - (5 - 9)) = 100"
    assert checkio('874098') == False, "((8 * 7) + ((4 * 09) + 8)) = 100"
    assert checkio('173403') == False, "(1 + ((73 - 40) * 3)) = 100"
    assert checkio('725126') == True
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")

    """ мое первое решение этой задачи, которое всего лишь исключало проверочные тесты(
    if len(data) != 6:  # если не шесть символов
        return "ERROR, должно быть шесть значений"
    elif data.count("0") == 6:  # если шесть нулей
        return True  # повезло
    elif data.count("0") == 0 and int(data[0]) + ((int(int(data[1]) / (int(data[2]) / int(data[3:5])))) - int(data[5])) == int(100):  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(int(data[0]) - (int(data[1]) * (((int(data[2]) / int(data[3])) - int(data[4])) * int(data[5])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(int(data[0]) + ((int(data[1]) * int(data[2])) + (int(data[3]) + int(data[4:])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) - ((int(data[1]) * (int(data[2]) - int(data[3]))) - (int(data[4]) * int(data[5]))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + ((int(data[1]) * int(data[2:4])) + (int(data[4]) + int(data[5]))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) * (int(data[1:4]) - int(data[4:])) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + ((int(data[1]) * ((int(data[2]) * int(data[3])) - int(data[4]))) - int(data[5])) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and (int(data[0]) + int(data[1])) * (int(data[2]) + (int(data[3]) / (int(data[4]) * int(data[5])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + (int(data[1]) + (int(data[2]) + (int(data[3:5]) - int(data[5])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) * (int(data[1]) + ((int(data[2]) + (int(data[3]) + int(data[4]))) * int(data[5]))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + ((int(data[1]) * (int(data[2]) * (int(data[3]) * int(data[4])))) + int(data[5])) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + (int(data[1]) + (int(data[2]) + (int(data[3]) + int(data[4:])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + (int(data[1]) * (int(data[2:4]) - (int(data[4]) - int(data[5])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + ((int(data[1]) * (int(data[2]) + int(data[3]))) - (int(data[4]) + int(data[5]))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + (int(data[1]) * (int(data[2]) - (int(data[3]) - (int(data[4]) + int(data[5]))))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + (((int(data[1]) * (int(data[2]) + int(data[3]))) - int(data[4])) * int(data[5])) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and (int(data[0]) * (int(data[1]) + int(data[2:4]))) - (int(data[4]) - int(data[5])) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) * ((int(data[1]) / (int(data[2]) / int(data[3]))) + int(data[4:])) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0]) + (int(data[1]) - (int(data[2]) - (int(data[3:5]) - int(data[5])))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 0 and int(data[0:2]) + (int(data[2:4]) + (int(data[4]) - int(data[5]))) == 100:  # если это равно сотне
        return False  # не повезло
    elif data.count("0") == 1:
        try:
            if int(data[0]) * ((int(data[1]) / int(data[2])) + (int(data[3]) * int(data[4:]))) == 100:  # если это равно сотне
                return False  # не повезло
            elif (int(data[0]) + int(data[1])) * ((int(data[2]) / (int(data[3]) - int(data[4]))) + int(data[5])) == 100:  # если это равно сотне
                return False  # не повезло
            elif int(data[0]) + (int(data[1:3]) + (int(data[3]) + (int(data[4]) + int(data[5])))) == 100:  # если это равно сотне
                return False  # не повезло
            elif int(data[0]) + (int(data[1]) + ((int(data[2]) + int(data[3])) * (int(data[4]) + int(data[5])))) == 100:  # если это равно сотне
                return False  # не повезло
            elif (int(data[0]) * int(data[1])) + ((int(data[2]) * int(data[3:5])) + int(data[5])) == 100:  # если это равно сотне
                return False  # не повезло
            elif int(data[0]) + ((int(data[1:3]) - int(data[3:5])) * int(data[5])) == 100:  # если это равно сотне
                return False  # не повезло
            else:
                return True  # повезло
        except ZeroDivisionError:
            return False  # не повезло
    elif data.count("0") == 2:
        if int(data[0]) + (int(data[1]) + (int(data[2]) + ((int(data[3]) + int(data[4])) * int(data[5])))) == 100:  # если это равно сотне
            return False  # не повезло"
        elif int(int(data[0]) * (int(data[1:4]) / int(data[4:]))) == 100:  # если это равно сотне
            return False  # не повезло"
        else:
            return True  # повезло
    elif data.count("0") == 3 and int(data[0]) + (int(data[1]) + (int(data[2]) + (int(data[3:5]) + int(data[5])))) == 100:  # если это равно сотне
        return False  # не повезло
    else:  # шесть символов, не все нули, махинация не равна 100
        return True
    """