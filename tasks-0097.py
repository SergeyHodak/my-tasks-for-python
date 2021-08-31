from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None, operating: Optional[timedelta] = None) -> int:
    """
    I Предварительное условие первой миссии с лампочками:
        - Массив нажатий на кнопку всегда отсортирован по возрастанию
        - В массиве нажатия кнопки нет повторяющихся элементов (значит результат всегда должен быть больше 0)
        - Количество элементов всегда четное (свет со временем погаснет)
        - Минимальная возможная дата - 01.01.1970.
        - Максимально возможная дата 9999-12-31

    II Добавлено время начала наблюдения (start_watching), как долго комната была освещена, с момента start_watching.

    III Добавлено - время окончания наблюдения (end_watching).
        Изменено - количество элементов (нажатий на кнопку) может быть нечетным.

    IV Теперь у нас более одной лампочки.
       В массиве переключения лампочек теперь может быть передан еще и номер лампочки, кнопка которой нажимается.
       Элемент массива нажатий на кнопку может быть или объект datetime (значит время нажатия на первую кнопку)
       или tuple из 2х элементов (где первый элементы — это объект datetime время нажатия на кнопку),
       а второй это номер лампочки, кнопка который нажимается.

    V +4ый аргумент - время работы лампочек. Аргумент времени работы передается как объект timedelta.
      По аналогии с предыдущими миссиями - если он не передан, значит лампа работает бесконечно.
    """
    def unlimited_space_with_lots_of_lamps(a, b, d, lamp_number, position_in_time):  # неограниченное пространство с большим количеством ламп
        if a[lamp_number] == 0:  # эта лампа не включена
            a[lamp_number] = 1  # в словарь этой лампы ставлю отметку что она включена
            c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
            if c.count("1") == 1:  # включена одна
                b = position_in_time  # сохраняю сюда время для старта калькуляции
        else:  # эта лампа включена
            a[lamp_number] = 0  # в словарь этой лампы ставлю отметку что она выключена
            c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
            if c.count("1") == 0:  # # все лампы выключены
                d += (position_in_time - b).total_seconds()  # записываем результат в секундах
        return a, b, d

    def limited_to_starting_with_a_lot_of_lamps(a, b, d, lamp_number, position_in_time, start_watching):  # ограничен стартом с большим количеством ламп
        if a[lamp_number] == 0:  # эта лампа не включена
            a[lamp_number] = 1  # в словарь отметим: включена
            if start_watching <= position_in_time:  # поз>=старта
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 1:  # включена одна
                    b = position_in_time  # сохраняю сюда время для старта калькуляции
        else:  # эта лампа включена
            a[lamp_number] = 0  # в словарь этой лампы ставлю отметку что она выключена
            if start_watching <= position_in_time:  # поз>=старта
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 0:  # # все лампы выключены
                    d += (position_in_time - b).total_seconds()  # записываем результат в секундах
        return a, b, d

    def a_piece_of_time_with_a_lot_of_lamps(a, b, d, lamp_number, position_in_time, start_watching, end_watching, i, els):  # кусок времени с большим количеством ламп
        flag_for_loop = 0  # флаг для сброса цикла
        if (start_watching <= position_in_time < end_watching) and (1 not in dict.values(a)):  # (старт <= поз < финиш) и (ни одна лампа еще не включена)
            a[lamp_number] = 1  # в словарь этой лампы ставлю отметку что она включена
            b = position_in_time  # сохраняю сюда время для старта калькуляции
        elif (start_watching <= position_in_time < end_watching) and (a[lamp_number] == 0):  # (старт <= поз < финиш) и (эта лампа не включена)
            a[lamp_number] = 1  # в словарь этой лампы ставлю отметку что она включена
            c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
            if c.count("1") == 1:  # включена одна
                b = position_in_time  # сохраняю сюда время для старта калькуляции
        elif position_in_time < start_watching and a[lamp_number] == 0:  # (поз < старт) и (эта лампа не включена)
            a[lamp_number] = 1  # в словарь этой лампы ставлю отметку что она включена
        elif (start_watching <= position_in_time <= end_watching) and (a[lamp_number] == 1):  # (старт <= поз <= финиш) и (эта лампа включена)
            a[lamp_number] = 0  # в словарь этой лампы ставлю отметку что она выключена
            if i == len(els) - 1:  # если это последний переключатель
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 0:  # если все лампы выключились
                    d += (position_in_time - b).total_seconds()  # записываем результат в секундах
                else:  # есть включенные лампы
                    d += (end_watching - b).total_seconds()  # записываем результат в секундах
            else:  # это не последний переключатель
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 0:  # если все лампы выключились
                    d += (position_in_time - b).total_seconds()  # записываем результат в секундах
        elif position_in_time < start_watching and a[lamp_number] == 1:  # если (поз < старт) и (эта лампа включена)
            a[lamp_number] = 0  # в словарь этой лампы ставлю отметку что она выключена
        elif end_watching <= position_in_time:  # если позиция больше либо равна финишу
            if a[lamp_number] == 1:  # если лампа включена
                d += (end_watching - b).total_seconds()  # записываем результат в секундах
                flag_for_loop = 1  # прервать цикл
            else:  # если лампа выключена
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 0:  # если все лампы выключились
                    flag_for_loop = 1  # прервать цикл
                else:  # если есть включенные лампы
                    d += (end_watching - b).total_seconds()  # записываем результат в секундах
                    flag_for_loop = 1  # прервать цикл
        return a, b, d, flag_for_loop

    def gap_plus_operation(a, b, d, lamp_number, position_in_time, start_watching, end_watching, i, els, operating):  # промежуток плюс эксплуатация
        flag_for_loop = 0  # флаг для сброса цикла
        if (start_watching <= position_in_time < end_watching) and (1 not in dict.values(a)):  # (старт <= поз < финиш) и (ни одна лампа еще не включена)
            if len([a[lamp_number]]) == 1:  # если данный ключ не изменялся и смеет в себе только одно значение, значит эта лампа еще не эксплуатировалась
                left_to_use = operating  # оставшаясь эксплуатация
            else:  # ключ имеет три переменных, значит лампа уже использовалась
                left_to_use = a[lamp_number][2]  # оставшаясь эксплуатация
            if left_to_use == 0:  # если лампа сгорела
                a[lamp_number] = 0, position_in_time, left_to_use  # в словарь этой лампы ставлю отметку что она выкл +время включения +оставшаяся эксплуатация
            else:  # лампа еще дишит
                a[lamp_number] = 1, position_in_time, left_to_use  # в словарь этой лампы ставлю отметку что она выкл +время включения +оставшаяся эксплуатация
                b = position_in_time  # сохраняю сюда время для старта калькуляции
        elif (start_watching <= position_in_time < end_watching) and (a[lamp_number] == 0):  # (старт <= поз < финиш) и (эта лампа не включена)
            if len([a[lamp_number]]) == 1:  # если данный ключ не изменялся и смеет в себе только одно значение, значит эта лампа еще не эксплуатировалась
                left_to_use = operating  # оставшаясь эксплуатация
            else:  # ключ имеет три переменных, значит лампа уже использовалась
                left_to_use = a[lamp_number][2]  # оставшаясь эксплуатация
            if left_to_use == 0:  # если лампа сгорела
                a[lamp_number] = 0, position_in_time, left_to_use  # в словарь этой лампы ставлю отметку что она выкл +время включения +оставшеяся эксплуатация
            else:  # лампа еще дишит
                a[lamp_number] = 1, position_in_time, left_to_use  # в словарь этой лампы ставлю отметку что она включена +время включения +оставшеяся эксплуатация
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 1:  # включена одна
                    b = position_in_time  # сохраняю сюда время для старта калькуляции
        elif position_in_time < start_watching and a[lamp_number] == 0:  # (поз < старт) и (эта лампа не включена)
            if len([a[lamp_number]]) == 1:  # если данный ключ не изменялся и смеет в себе только одно значение, значит эта лампа еще не эксплуатировалась
                left_to_use = operating  # оставшаясь эксплуатация
            else:  # ключ имеет три переменных, значит лампа уже использовалась
                left_to_use = a[lamp_number][2]  # оставшаясь эксплуатация
            if left_to_use == 0:  # если лампа сгорела
                a[lamp_number] = 0, position_in_time, left_to_use  # в словарь этой лампы ставлю отметку что она выкл +время включения +оставшеяся эксплуатация
            else:  # лампа еще дишит
                a[lamp_number] = 1, position_in_time, left_to_use  # в словарь этой лампы ставлю отметку что она включена +время включения +оставшеяся эксплуатация



        elif (start_watching <= position_in_time <= end_watching) and (a[lamp_number] == 1):  # (старт <= поз <= финиш) и (эта лампа включена)
            y = (a[lamp_number][2] - (position_in_time - a[lamp_number][1])).total_seconds()  # оставшийся строк службы - (поз сейчас - поз вкл этой лампы)
            print("тест минусовок1=", y)

            a[lamp_number] = 0  # в словарь этой лампы ставлю отметку что она выключена
            print("a1=", a)
            print("тест на инфу:", a[lamp_number], "0=", a[lamp_number][0], "1=", a[lamp_number][1])
            if i == len(els) - 1:  # если это последний переключатель
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 0:  # если все лампы выключились
                    d += (position_in_time - b).total_seconds()  # записываем результат в секундах
                else:  # есть включенные лампы
                    d += (end_watching - b).total_seconds()  # записываем результат в секундах
            else:  # это не последний переключатель
                c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                if c.count("1") == 0:  # если все лампы выключились
                    d += (position_in_time - b).total_seconds()  # записываем результат в секундах



        elif position_in_time < start_watching and a[lamp_number] == 1:  # если (поз < старт) и (эта лампа включена)
            y = (a[lamp_number][2] - (position_in_time - a[lamp_number][1])).total_seconds()  # оставшийся строк службы - (поз сейчас - поз вкл этой лампы)
            print("тест минусовок2=", y)

            a[lamp_number] = 0  # , position_in_time  # в словарь этой лампы ставлю отметку что она выключена
            print("a2=", a)



        elif end_watching <= position_in_time:  # если позиция больше либо равна финишу
            y = a[lamp_number][2] - (position_in_time - a[lamp_number][1])  # оставшийся строк службы - (поз сейчас - поз вкл этой лампы)
            if str(type(y)) == "<class 'datetime.timedelta'>":
                y = y.total_seconds()
            elif str(type(y)) == "<class 'datetime.datetime'>":
                y = y.second
            if int(y) >= 0:  # лампа жива
                if a[lamp_number] == 1:  # если лампа включена
                    d += (end_watching - b).total_seconds()  # записываем результат в секундах
                    flag_for_loop = 1  # прервать цикл
                else:  # если лампа выключена
                    c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                    if c.count("1") == 0:  # если все лампы выключились
                        flag_for_loop = 1  # прервать цикл
                    else:  # если есть включенные лампы
                        d += (end_watching - b).total_seconds()  # записываем результат в секундах
                        flag_for_loop = 1  # прервать цикл
            else:  # лампа за этот период сгорела
                pos = a[lamp_number][1] + a[lamp_number][2]  # замещаем позицию отключения лампы и ее перегорание (поз вкл этой лампы + оставшийся строк службы)
                if a[lamp_number] == 1:  # если лампа включена + когдато сгорела по пути к этой отметке
                    if end_watching <= pos:  # если новая позиция больше либо равна финишу
                        if a[lamp_number] == 1:  # если лампа включена
                            d += (end_watching - b).total_seconds()  # записываем результат в секундах
                            flag_for_loop = 1  # прервать цикл
                        else:  # если лампа выключена
                            c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                            if c.count("1") == 0:  # если все лампы выключились
                                flag_for_loop = 1  # прервать цикл
                            else:  # если есть включенные лампы
                                d += (end_watching - b).total_seconds()  # записываем результат в секундах
                                flag_for_loop = 1  # прервать цикл
                    else:  # если новая позиция меньше финиша
                        if a[lamp_number] == 1:  # если лампа включена
                            d += (pos - b).total_seconds()  # записываем результат в секундах
                            flag_for_loop = 1  # прервать цикл
                        else:  # если лампа выключена
                            c = str(dict.values(a))  # создаем форму для проверки сколько ламп зажжено
                            if c.count("1") == 0:  # если все лампы выключились
                                flag_for_loop = 1  # прервать цикл
                            else:  # если есть включенные лампы, нужно проверить есть ли досветившаясь до финиша
                                res = 0  # на всякий пожарный
                                for x in a:  # пробежка по всем лампам в поисках зажженных
                                    if a[x][0] == 1:  # если эта лампа осталась включенной, дожила ли она к финишу
                                        y_f = (a[x][2] - (end_watching - a[x][1])).total_seconds()  # оставшийся строк службы - (поз сейчас - поз вкл этой лампы)
                                        if y_f >= 0:  # лампа жива
                                            d += (end_watching - b).total_seconds()  # записываем результат в секундах
                                            res = 0  # обнулить если есть такой выброс
                                            break  # прервать этот цикл
                                        else:  # лампа не дожила к финишу, но а вдруг есть еще такая не дожившая но она просветилась дольше этой?
                                            lamp_burned_out = a[x][1] - a[x][2]  # лампа перегорела в такоето время (поз вкл этой лампы - оставшийся строк службы)
                                            if lamp_burned_out > res:  # если эта лампа проработала дольше чем предыдущая
                                                res = lamp_burned_out  # записываем это время в переменную
                                if res != 0:  # если результат не сброшен
                                    d += (res - b).total_seconds()  # записываем результат в секундах
                                flag_for_loop = 1  # прервать цикл вызывающий эту подфункцию
        return a, b, d, flag_for_loop

    L = 0  # флаг того что здесь нету типа данных "tuple"
    for i in range(0, len(els)):  # пробежка по els
        if type(els[i]) == tuple:  # если здесь тип tuple
            L += 1  # записать в флаг
            break  # прекратить цикл
    if L == 0:  # если этот запрос только с одной лампой
        if not end_watching:  # если нет времени окончания подсчета
                if not start_watching:  # если нет времени начала подсчета
                    if operating == None:  # если нет ограничения на эксплуатацию
                        a = 0  # аргумент на вывод
                        for i in range(0, len(els), 2):  # пробежка по els от нуля до конца с шагом 2
                            a += (els[i + 1] - els[i]).total_seconds()  # от старшего отнимаем меншее.вытягиваем с этого объекта секунды
                        return int(a)  # преврящает число внутри скобок, в целое. и отправляем получателю
                    else:  # есть ограничение, с указанием сколько проработает лампа во включенном состоянии
                        a = 0  # для подсчета времени освещенности
                        b = 0  # старт свечения лампы
                        ost = operating  # оставшееся время работы лампы
                        for i in range(0, len(els), 1):  # пробежка по els от нуля до конца с шагом 1
                            if i % 2 == 0:  # четное, значит здесь лампу вкл
                                b = els[i]  # записали время когда лапу включили
                            else:  # нечетное, значти здесь лампу выкл
                                prom = els[i] - b  # получаем промежуток времени включенной лампы
                                if prom >= ost:  # если получившийся отрезок больше оставшегося времени свечения лампы
                                    a += (ost).total_seconds()  # записать данные
                                    break  # прервать цикл
                                else:  # полученный отрезок меньше строка работы лампы
                                    a += (els[i] - b).total_seconds()  # записать данные
                        return int(a)  # преврящает число внутри скобок, в целое. и отправляем получателю
                else:  # есть время подсчета
                    a = 0  # аргумент на вывод
                    for i in range(0, len(els), 2):  # пробежка по els от нуля до конца с шагом 2
                        if els[i + 1] > start_watching and els[i] > start_watching:  # 1 и 2 аргументы больше старта
                            a += (els[i + 1] - els[i]).total_seconds()  # от старшего отнимаем меншее.вытягиваем секунды
                        elif els[i + 1] > start_watching >= els[i]:  # если старт между аргументами
                            a += (els[i + 1] - start_watching).total_seconds()  # от старшего отнимаем стартовое
                    return int(a)  # преврящает число внутри скобок, в целое. и отправляем получателю
        else:  # есть время окончания подсчета
            a = 0  # для хранения в себе информации о включенной лампе, в данном диапазоне времени
            for i in range(0, len(els), 1):  # пробежка по els от нуля до конца с шагом 1
                if i % 2 == 0:  # при четной позиции лампа включается
                    if start_watching < els[i] < end_watching and i == len(els) - 1:  # между, и последняя
                        a += (end_watching - els[i]).total_seconds()  # записываем результат в секундах
                    elif i == len(els) - 1 and start_watching > els[i] and end_watching > els[i]:  # если поз последняя и (старт и финиш больше этой позиции)
                        a += (end_watching - start_watching).total_seconds()  # записываем результат в секундах
                else:  # при нечетной лампа выключается
                    if start_watching < els[i] < end_watching and start_watching < els[i - 1]:  # между, и поз-1>старт
                        a += (els[i] - els[i - 1]).total_seconds()  # записываем результат в секундах
                    elif (start_watching < els[i] < end_watching) and (start_watching > els[i - 1]):  # между, и поз-1 < старт
                        a += (els[i] - start_watching).total_seconds()  # записываем результат в секундах
                    elif (end_watching < els[i]) and (start_watching < els[i - 1]) and (end_watching > els[i - 1]):  # позиция больше финишного маркера, пред поз больше стартового маркера, и финиш больше пред поз
                        a += (end_watching - els[i - 1]).total_seconds()  # записываем результат в секундах
                    elif (end_watching < els[i] and els[i - 1] < start_watching) or \
                            (end_watching == els[i] and start_watching == els[i - 1]) or \
                            (end_watching < els[i] and els[i - 1] == start_watching) or \
                            (end_watching == els[i] and els[i - 1] < start_watching):  # (отрезок с обеих строн вылазит за мпромежуток маркеров) или (если позиции совпадают с маркерами) или (если поз больше финиша и пред поз равна стартовому) или (поз = финишу и старт больше пред поз)
                        a += (end_watching - start_watching).total_seconds()  # записываем результат в секундах
            return int(a)  # преврящает число внутри скобок, в целое. и отправляем получателю
    else:
        if operating == None:  # если здесь без таймера на "выкинь и купи новую, дай нам заработать больше чем ты себе можешь представить"
            a = {}  # создадим словарь для состояния ламп
            for i in range(0, len(els)):  # пробежка по кнопкам
                if type(els[i]) == tuple:  # если здесь тип tuple
                    a[els[i][1]] = 0  # номер лампы или кнопка, и состояние выкл=0
                else:  # здесь объект datetime
                    a["без номера"] = 0  # лампа которой не указали номер, и ее состояние выкл=0

            d = 0  # переменная для хранения времени на выдачу
            b = 0  # на всякий пожарный
            if start_watching == None and end_watching == None:  # если старт и финиш не заданы
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a, b, d = unlimited_space_with_lots_of_lamps(a, b, d, els[i][1], els[i][0])
                    else:  # здесь объект datetime
                        a, b, d = unlimited_space_with_lots_of_lamps(a, b, d, "без номера", els[i])
                return int(d)

            if end_watching == None:  # если финиш не задан
                b = start_watching  # на всякий пожарный
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a, b, d = limited_to_starting_with_a_lot_of_lamps(a, b, d, els[i][1], els[i][0], start_watching)
                    else:  # здесь объект datetime
                        a, b, d = limited_to_starting_with_a_lot_of_lamps(a, b, d, "без номера", els[i], start_watching)
                return int(d)

            b = start_watching  # на всякий пожарный
            for i in range(0, len(els)):  # пробежка по кнопкам
                if type(els[i]) == tuple:  # если здесь тип tuple
                    a, b, d, flag_for_loop = a_piece_of_time_with_a_lot_of_lamps(a, b, d, els[i][1], els[i][0], start_watching, end_watching, i, els)
                    if flag_for_loop == 1:  # если активирован флаг прерыва цикла
                        break  # прервать цикл
                else:  # здесь объект datetime
                    a, b, d, flag_for_loop = a_piece_of_time_with_a_lot_of_lamps(a, b, d, "без номера", els[i], start_watching, end_watching, i, els)
                    if flag_for_loop == 1:  # если активирован флаг прерыва цикла
                        break  # прервать цикл
            return int(d)
        else:  # покупай лампы и корми производителей этих ламп
            # нужен варик для без старта и без финиша с множеством ламп, и строком эксплуатации!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if start_watching == None and end_watching == None:  # работа ламп не в ограниченном промежутке времени
                a = {}  # создадим словарь для состояния ламп
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a[els[i][1]] = 0, 0, operating  # номер лампы или кнопка, и состояние выкл=0
                    else:  # здесь объект datetime
                        a["без номера"] = 0, 0, operating  # лампа которой не указали номер, и ее состояние выкл=0

                c = 0  # для калькуляции
                for f in range(0, len(els)):  # пробежка по выключателям
                    if type(els[f]) == tuple:  # если здесь тип tuple
                        if a[els[f][1]][0] == 0:  # если лампа выкл
                            res = a[els[f][1]][2]  # дублировать ресурс на использование лампы
                            a[els[f][1]] = 1, els[f][0], res  # вкл лампу, когда включили, ее оставшийся ресурс
                            if f == len(els)-1:  # если это последняя позиция
                                c += res.total_seconds()  # записать время
                        else:  # лампа включена
                            res = a[els[f][1]][2] - (els[f][0] - a[els[f][1]][1])  # ресурс - (сейчас - когда была включена)
                            if str(type(res)) == "<class 'datetime.timedelta'>":  # в зависимости от типа
                                res = res.total_seconds()
                            elif str(type(res)) == "<class 'datetime.datetime'>":  # в зависимости от типа
                                res = res.second
                            if int(res) >= 0:  # лампа жива еще
                                c += (els[f][0] - a[els[f][1]][1]).total_seconds()  # записать время
                                a[els[f][1]] = 0, 0, res  # выкл лампу, когда включили, ее оставшийся ресурс
                            else:  # до момента выключения лампа умерла уже
                                c += res.total_seconds()  # записать время
                                a[els[f][1]] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                    else:  # другие типы (например: datetime)
                        if a["без номера"][0] == 0:  # если лампа выкл
                            res = a["без номера"][2]  # дублировать ресурс на использование лампы
                            a["без номера"] = 1, els[f], res  # вкл лампу, когда включили, ее оставшийся ресурс
                            if f == len(els) - 1:  # если это последняя позиция
                                c += res.total_seconds()  # записать время
                        else:  # лампа включена
                            res = a["без номера"][2] - (els[f] - a["без номера"][1])  # ресурс - (сейчас - когда была включена)
                            if str(type(res)) == "<class 'datetime.timedelta'>":  # в зависимости от типа
                                res = res.total_seconds()
                            elif str(type(res)) == "<class 'datetime.datetime'>":  # в зависимости от типа
                                res = res.second
                            if int(res) >= 0:  # лампа жива еще
                                c += (els[f] - a["без номера"][1]).total_seconds()  # записать время
                                a["без номера"] = 0, 0, res  # выкл лампу, когда включили, ее оставшийся ресурс
                            else:  # до момента выключения лампа умерла уже
                                c += res.total_seconds()  # записать время
                                a["без номера"] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                return int(c)
            else:  # ограничено стартом и финишом наблюдения за освещенностю
                a = {}  # создадим словарь для состояния ламп
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a[els[i][1]] = 0, end_watching, start_watching  # номер лампы или кнопка, и состояние выкл=0
                    else:  # здесь объект datetime
                        a["без номера"] = 0, end_watching, start_watching  # лампа которой не указали номер, и ее состояние выкл=0

                d = 0  # на всякий пожарный
                b = start_watching  # на всякий пожарный
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a, b, d, flag_for_loop = gap_plus_operation(a, b, d, els[i][1], els[i][0], start_watching, end_watching, i, els, operating)
                        if flag_for_loop == 1:  # если активирован флаг прерыва цикла
                            break  # прервать цикл
                    else:  # здесь объект datetime
                        a, b, d, flag_for_loop = gap_plus_operation(a, b, d, "без номера", els[i], start_watching, end_watching, i, els, operating)
                        if flag_for_loop == 1:  # если активирован флаг прерыва цикла
                            break  # прервать цикл
                return int(d)


if __name__ == '__main__':
    print("Пример:")
    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                     datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                    operating=timedelta(seconds=100)), "должно вернутся 60")

    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)],
                    operating=timedelta(seconds=5)), "должно вернутся 5")

    print(sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                     (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                    start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
                    operating=timedelta(seconds=5)), "должно вернутся 10")


    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                      datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)]) == 60
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10),
                      (datetime(2015, 1, 12, 11, 0, 0), 2), (datetime(2015, 1, 12, 11, 1, 0), 2)]) == 70
    assert sum_light([datetime(2015, 1, 12, 10, 0, 20), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)]) == 30
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)]) == 40
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                      (datetime(2015, 1, 12, 10, 1, 0), 3), (datetime(2015, 1, 12, 10, 1, 20), 3)]) == 60
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                      datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                     datetime(2015, 1, 12, 10, 0, 50)) == 10
    assert sum_light([datetime(2015, 1, 12, 10, 0, 20), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 30)) == 20
    assert sum_light([datetime(2015, 1, 12, 10, 0, 20), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 20)) == 30
    assert sum_light([datetime(2015, 1, 12, 10, 0, 20), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 10)) == 30
    assert sum_light([datetime(2015, 1, 12, 10, 0, 20), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 50)) == 0
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 30)) == 20
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 20)) == 30
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                      (datetime(2015, 1, 12, 10, 1, 20), 2), (datetime(2015, 1, 12, 10, 1, 40), 2)],
                     datetime(2015, 1, 12, 10, 0, 20)) == 50
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                      datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                     datetime(2015, 1, 12, 10, 0, 30), datetime(2015, 1, 12, 10, 1, 0)) == 30
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                      datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                     datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                      datetime(2015, 1, 12, 10, 0, 10)], datetime(2015, 1, 12, 10, 0, 0),
                     datetime(2015, 1, 12, 10, 0, 30)) == 30
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0)) == 40
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)) == 0
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2)],
                     datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                     datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                     datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 30)) == 20
    assert sum_light(els=[(datetime(2015, 1, 11, 0, 0, 0), 3), datetime(2015, 1, 12, 0, 0, 0),
                          (datetime(2015, 1, 13, 0, 0, 0), 3), (datetime(2015, 1, 13, 0, 0, 0), 2),
                          datetime(2015, 1, 14, 0, 0, 0), (datetime(2015, 1, 15, 0, 0, 0), 2)],
                     start_watching=datetime(2015, 1, 10, 0, 0, 0),
                     end_watching=datetime(2015, 1, 16, 0, 0, 0)) == 345600
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)],
                     operating=timedelta(seconds=100)) == 10
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)],
                     operating=timedelta(seconds=5)) == 5
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10),
                      (datetime(2015, 1, 12, 10, 0, 0), 2), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                     operating=timedelta(seconds=100)) == 60
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30),
                      (datetime(2015, 1, 12, 10, 0, 30), 2), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                     operating=timedelta(seconds=100)) == 60
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30),
                      (datetime(2015, 1, 12, 10, 0, 30), 2), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                     operating=timedelta(seconds=20)) == 40
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                      (datetime(2015, 1, 12, 10, 1, 0), 3), (datetime(2015, 1, 12, 10, 1, 20), 3)],
                     operating=timedelta(seconds=10)) == 30
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                      (datetime(2015, 1, 12, 10, 1, 20), 2), (datetime(2015, 1, 12, 10, 1, 40), 2)],
                     start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                      datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                      (datetime(2015, 1, 12, 10, 1, 20), 2), (datetime(2015, 1, 12, 10, 1, 40), 2)],
                     start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=10)) == 20
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                     start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
                     operating=timedelta(seconds=20)) == 20
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                     start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
                     operating=timedelta(seconds=10)) == 20
    assert sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                      (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                     start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
                     operating=timedelta(seconds=5)) == 10
    print("Пьятая миссия серии завершена? Нажмите 'Check', чтобы получить отличные награды!")