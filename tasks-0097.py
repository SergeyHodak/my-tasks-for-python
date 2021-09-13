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
    global exposure_time, exposure_time, lamp_name

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
        if operating == None:  # если здесь без таймера на пригодность лампы
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
        else:  # есть таймер ограничивающий пригодность лампы
            if start_watching == None and end_watching == None:  # работа ламп не в ограниченном промежутке времени
                a = {}  # создадим словарь для состояния ламп
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a[els[i][1]] = 0, 0, operating  # номер лампы или кнопка, и состояние выкл=0, когда включили, ее оставшийся ресурс
                    else:  # здесь объект datetime
                        a["без номера"] = 0, 0, operating  # лампа которой не указали номер, и ее состояние выкл=0, когда включили, ее оставшийся ресурс

                c = 0  # для калькуляции
                light_sensor = 0  # типа (световой датчик)
                for f in range(0, len(els)):  # пробежка по выключателям
                    if type(els[f]) == tuple:  # если здесь тип tuple
                        tt_1 = els[f][1]  # номер лампы
                        kk_1 = els[f][0]  # дата нажатия на кнопу
                    else:  # другие типы (например: datetime)
                        tt_1 = "без номера"  # номер лампы
                        kk_1 = els[f]  # дата нажатия на кнопу
                    if a[tt_1][0] == 0:  # если лампа выкл
                        if type(a[tt_1][2]) == timedelta:  # если здесь тип datetime.timedelta
                            res = (a[tt_1][2]).total_seconds()  # дублировать ресурс на использование лампы
                        elif type(a[tt_1][2]) == int:  # если здесь тип int
                            res = a[tt_1][2]  # дублировать ресурс на использование лампы
                        if a[tt_1][2] != 0:  # если эта лампа еще живая
                            a[tt_1] = 1, kk_1, res  # вкл лампу, когда включили, ее оставшийся ресурс
                        else:  # лампа сгорела, она не заработает больше
                            continue  # продолжить с начала
                        if f == len(els)-1:  # если это последняя позиция
                            c += res  # записать время которое осталось для этой лампы
                        else:  # это не последняя позиция
                            g = []  # создаем форму для проверки сколько ламп зажжено
                            for kofd in a:  # пробежка по словарю
                                g.append(a[kofd][0])  # записать состояние рубильника лампы
                            if g.count(1) == 1:  # если включена только одна лампа
                                light_sensor = kk_1  # запись времени начала освещенности помещения
                            else:  # есть еще включенные лампы, дожили ли они к этому времени, не прерывая наблюдение датчика за освещенностью
                                m = light_sensor + timedelta(seconds=res)  # время когда датчик последний раз стал записывать + ресурс данной лампы в позиции
                                for u in a:  # пробежка по включенным лампам
                                    if type(a[u]) == tuple:  # если здесь тип tuple
                                        tt_2 = u  # тип используемого ключа, дальше в цикле
                                    else:  # другие типы (например: datetime)
                                        tt_2 = "без номера"  # тип используемого ключа, дальше в цикле
                                    if a[tt_2][0] == 1:  # если лампа вкл
                                        res = timedelta(seconds=a[tt_2][2]) - (kk_1 - a[tt_2][1])  # ресурс - (сейчас - когда была включена)
                                        if type(res) == timedelta:  # в зависимости от типа
                                            res = res.total_seconds()  # превращение в секунды
                                        elif type(res) == datetime:  # в зависимости от типа
                                            res = res.second  # превращение в секунды
                                        if int(res) > 0:  # лампа еще жива
                                            m = kk_1  # отметить как непреодолимую планку для других
                                        elif int(res) == 0:  # лампа дожила к этой точке и сдохла
                                            m = kk_1  # отметить как непреодолимую планку для других
                                            a[u] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                                        else:  # не до жила
                                            if res > m.second:  # если она проработала дольше чем другие
                                                m = light_sensor + res  # отметить ее время перегорания для сравнения с другими
                                                a[u] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                                if m == kk_1:  # если последняя потухшая лампа совпадает с точкой измерения
                                    if a[tt_1] != (0, 0, 0):  # если канешно эта лампа не сгоревшая
                                        c += (m - light_sensor).total_seconds()  # записать в секундах
                                        light_sensor = m  # обновить позицию датчика
                    else:  # лампа включена
                        res = a[tt_1][2] - (kk_1 - a[tt_1][1]).total_seconds()  # ресурс - (сейчас - когда была включена)
                        if type(res) == timedelta:  # в зависимости от типа
                            res = res.total_seconds()  # превращение в секунды
                        elif type(res) == datetime:  # в зависимости от типа
                            res = res.second  # превращение в секунды
                        if int(res) >= 0:  # лампа еще жива
                            a[tt_1] = 0, 0, int(res)  # выкл лампу, когда включили, ее оставшийся ресурс
                            g = []  # создаем форму для проверки сколько ламп зажжено
                            for kofd in a:  # пробежка по словарю
                                g.append(a[kofd][0])  # записать состояние рубильника лампы
                            if g.count(1) == 0:  # выключены все лампы
                                hak = kk_1 - light_sensor
                                if type(hak) == timedelta:  # в зависимости от типа
                                    hak = hak.total_seconds()  # превращение в секунды
                                elif type(hak) == datetime:  # в зависимости от типа
                                    hak = hak.second  # превращение в секунды
                                c += hak  # записать время
                                light_sensor = 0  # обнуление датчика
                        else:  # до момента выключения лампа умерла уже
                            save_resource = a[tt_1][2]  # сохранить ресурс
                            a[tt_1] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                            g = []  # создаем форму для проверки сколько ламп зажжено
                            for kofd in a:  # пробежка по словарю
                                g.append(a[kofd][0])  # записать состояние рубильника лампы
                            if g.count(1) > 0:  # если после выключения еще остались вкл лампы
                                m = light_sensor + timedelta(seconds=save_resource)  # для сравнения если ни одна не догорела к моменту выкл, но есть которая дольше всех просветилась
                                for u in range(0, len(els)):  # пробежка по включенным лампам
                                    if type(els[u]) == tuple:  # если здесь тип tuple
                                        tt_2 = els[u][1]
                                    else:  # другие типы (например: datetime)
                                        tt_2 = "без номера"
                                    if a[tt_2][0] == 1:  # если лампа вкл
                                        res = timedelta(seconds=a[tt_2][2]) - (kk_1 - a[tt_2][1])  # ресурс - (сейчас - когда была включена)
                                        if type(res) == timedelta:  # в зависимости от типа
                                            res = res.total_seconds()  # превращение в секунды
                                        elif str(type(res)) == "<class 'datetime.datetime'>":  # в зависимости от типа
                                            res = res.second  # превращение в секунды
                                        if int(res) >= 0:  # лампа еще жива
                                            m = kk_1  # отметить как непреодолимую планку для других
                                        else:  # не до жила
                                            if (a[tt_2][2] - (kk_1 - a[tt_2][1])) > m:  # если она проработала дольше чем другие
                                                m = light_sensor + res  # отметить ее время перегорания для сравнения с другими
                                if m == kk_1:  # если последняя потухшая лампа совпадает с точкой измерения
                                    if a[tt_1] != (0, 0, 0):  # если канешно эта лампа не сгоревшая
                                        c += (kk_1 - a[tt_1][1]).total_seconds()
                                        light_sensor = kk_1  # обновление записи времени начала освещенности помещения
                            else:  # выключены все лампы
                                c += save_resource  # записать время
                                light_sensor = 0  # обнуление датчика
                return int(c)
            elif end_watching == None:  # нет флага о том когда нужно закончить наблюдение
                a = {}  # создадим словарь для состояния ламп
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a[els[i][1]] = 0, 0, int(operating.total_seconds())  # 'номер лампы': (состояние выкл=0, когда включили, ее оставшийся ресурс)
                    else:  # здесь объект datetime
                        a["без номера"] = 0, 0, int(operating.seconds)  # 'номер лампы': (состояние выкл=0, когда включили, ее оставшийся ресурс)

                c = 0  # сколько по времени было освещено помещение
                light_sensor = 0  # датчик света
                for f in range(0, len(els)):  # пробежка по выключателям
                    if type(els[f]) == tuple:  # если здесь тип tuple
                        tt_1 = els[f][1]  # номер лампы
                        dat_1 = els[f][0]  # дата нажатия на кнопу
                    else:  # другие типы (например: datetime)
                        tt_1 = "без номера"  # номер лампы
                        dat_1 = els[f]  # дата нажатия на кнопу

                    if dat_1 < start_watching:  # если позиция меньше начала включения датчика для наблюдения
                        if a[tt_1][0] == 1:  # если лампа включена
                            a[tt_1] = 0, 0, a[tt_1][2]  # 'номер лампы': (состояние выкл=0, когда включили, ее оставшийся ресурс)
                        else:  # если лампа выключена
                            a[tt_1] = 1, dat_1, a[tt_1][2]  # 'номер лампы': (состояние вкл=1, когда включили, ее оставшийся ресурс)
                        continue  # продолжить с начала

                    if a[tt_1][0] == 0:  # если лампа выкл
                        if type(a[tt_1][2]) == timedelta:  # если здесь тип datetime.timedelta
                            res = (a[tt_1][2]).total_seconds()  # дублировать ресурс на использование лампы
                        elif type(a[tt_1][2]) == int:  # если здесь тип int
                            res = a[tt_1][2]  # дублировать ресурс на использование лампы

                        if a[tt_1][2] != 0:  # если эта лампа еще живая
                            a[tt_1] = 1, dat_1, res  # вкл лампу, когда включили, ее оставшийся ресурс
                        else:  # лампа сгорела, она не заработает больше
                            continue  # продолжить с начала

                        if f == len(els) - 1:  # если это последняя позиция
                            c += res  # записать время которое осталось для этой лампы
                        else:  # это не последняя позиция
                            g = []  # создаем форму для проверки сколько ламп зажжено
                            for kofd in a:  # пробежка по словарю
                                g.append(a[kofd][0])  # записать состояние рубильника лампы

                            if g.count(1) == 1:  # если включена только одна лампа
                                light_sensor = dat_1  # запись времени начала освещенности помещения
                            else:  # есть еще включенные лампы, дожили ли они к этому времени, не прерывая наблюдение датчика за освещенностью
                                if dat_1 == start_watching:  # если время позиции равно время вкл датчика записи света
                                    light_sensor = start_watching  # включить датчик

                                m = light_sensor + timedelta(seconds=res)  # время когда датчик последний раз стал записывать + ресурс данной лампы в позиции
                                for u in a:  # пробежка по включенным лампам
                                    if type(a[u]) == tuple:  # если здесь тип tuple
                                        tt_2 = u  # тип используемого ключа, дальше в цикле
                                    else:  # другие типы (например: datetime)
                                        tt_2 = "без номера"  # тип используемого ключа, дальше в цикле
                                    if a[tt_2][0] == 1:  # если лампа вкл
                                        res = timedelta(seconds=a[tt_2][2]) - (dat_1 - a[tt_2][1])  # ресурс - (сейчас - когда была включена)
                                        if type(res) == timedelta:  # в зависимости от типа
                                            res = res.total_seconds()  # превращение в секунды
                                        elif type(res) == datetime:  # в зависимости от типа
                                            res = res.second  # превращение в секунды
                                        if int(res) > 0:  # лампа еще жива
                                            m = dat_1  # отметить как непреодолимую планку для других
                                        elif int(res) == 0:  # лампа дожила к этой точке и сдохла
                                            m = dat_1  # отметить как непреодолимую планку для других
                                            a[u] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                                        else:  # не до жила
                                            if res > m.second:  # если она проработала дольше чем другие
                                                m = light_sensor + res  # отметить ее время перегорания для сравнения с другими
                                                a[u] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                                if m == dat_1:  # если последняя потухшая лампа совпадает с точкой измерения
                                    if a[tt_1] != (0, 0, 0):  # если канешно эта лампа не сгоревшая
                                        c += (m - light_sensor).total_seconds()  # записать в секундах
                                        light_sensor = m  # обновить позицию датчика
                    else:  # лампа включена
                        res = a[tt_1][2] - (dat_1 - a[tt_1][1]).total_seconds()  # ресурс - (сейчас - когда была включена)
                        if type(res) == timedelta:  # в зависимости от типа
                            res = res.total_seconds()  # превращение в секунды
                        elif type(res) == datetime:  # в зависимости от типа
                            res = res.second  # превращение в секунды
                        if int(res) >= 0:  # лампа еще жива
                            a[tt_1] = 0, 0, int(res)  # выкл лампу, когда включили, ее оставшийся ресурс
                            g = []  # создаем форму для проверки сколько ламп зажжено
                            for kofd in a:  # пробежка по словарю
                                g.append(a[kofd][0])  # записать состояние рубильника лампы
                            if g.count(1) == 0:  # выключены все лампы
                                hak = dat_1 - light_sensor
                                if type(hak) == timedelta:  # в зависимости от типа
                                    hak = hak.total_seconds()  # превращение в секунды
                                elif type(hak) == datetime:  # в зависимости от типа
                                    hak = hak.second  # превращение в секунды
                                c += hak  # записать время
                                light_sensor = 0  # обнуление датчика
                        else:  # до момента выключения лампа умерла уже
                            save_resource = a[tt_1][2]  # сохранить ресурс
                            a[tt_1] = 0, 0, 0  # выкл лампу, когда включили, ее оставшийся ресурс
                            g = []  # создаем форму для проверки сколько ламп зажжено
                            for kofd in a:  # пробежка по словарю
                                g.append(a[kofd][0])  # записать состояние рубильника лампы
                            if g.count(1) > 0:  # если после выключения еще остались вкл лампы
                                m = light_sensor + timedelta(seconds=save_resource)  # для сравнения если ни одна не догорела к моменту выкл, но есть которая дольше всех просветилась
                                for u in range(0, len(els)):  # пробежка по включенным лампам
                                    if type(els[u]) == tuple:  # если здесь тип tuple
                                        tt_2 = els[u][1]
                                    else:  # другие типы (например: datetime)
                                        tt_2 = "без номера"
                                    if a[tt_2][0] == 1:  # если лампа вкл
                                        res = timedelta(seconds=a[tt_2][2]) - (dat_1 - a[tt_2][1])  # ресурс - (сейчас - когда была включена)
                                        if type(res) == timedelta:  # в зависимости от типа
                                            res = res.total_seconds()  # превращение в секунды
                                        elif str(type(
                                                res)) == "<class 'datetime.datetime'>":  # в зависимости от типа
                                            res = res.second  # превращение в секунды
                                        if int(res) >= 0:  # лампа еще жива
                                            m = dat_1  # отметить как непреодолимую планку для других
                                        else:  # не до жила
                                            if (a[tt_2][2] - (dat_1 - a[tt_2][1])) > m:  # если она проработала дольше чем другие
                                                m = light_sensor + res  # отметить ее время перегорания для сравнения с другими
                                if m == dat_1:  # если последняя потухшая лампа совпадает с точкой измерения
                                    if a[tt_1] != (0, 0, 0):  # если канешно эта лампа не сгоревшая
                                        c += (dat_1 - a[tt_1][1]).total_seconds()
                                        light_sensor = dat_1  # обновление записи времени начала освещенности помещения
                            else:  # выключены все лампы
                                c += save_resource  # записать время
                                light_sensor = 0  # обнуление датчика
                return int(c)
            else:  # ограничено стартом и финишом наблюдения за освещенностю
                a = {}  # создадим словарь для состояния ламп
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        a[els[i][1]] = 0, 0, int(operating.total_seconds())  # 'номер лампы': (состояние выкл=0, когда включили, ее оставшийся ресурс)
                    else:  # здесь объект datetime
                        a["без номера"] = 0, 0, int(operating.seconds)  # 'номер лампы': (состояние выкл=0, когда включили, ее оставшийся ресурс)

                lighting_duration = 0  # продолжительность освещения помещения
                light_sensor = 0  # датчик изначально пустое значение наблюдений
                for i in range(0, len(els)):  # пробежка по кнопкам
                    if type(els[i]) == tuple:  # если здесь тип tuple
                        lamp_name, exposure_time = els[i][1], els[i][0]  # имя_лампы, время_воздействия на эту лампу
                    elif type(els[i]) == datetime:  # если здесь тип datetime
                        lamp_name, exposure_time = "без номера", els[i]  # имя_лампы, время_воздействия на эту лампу

                    lamps_condition = []  # список для состояний ламп (вкл/выкл)
                    for lamp in a:  # пробежка по словарю, с информацией про лампы
                        lamps_condition.append(a[lamp][0])  # добавить состояние лампы в список

                    if exposure_time < start_watching:  # если воздействие попадет так что оно происходить раньше чем подадут питание на датчик
                        if i != len(els)-1:  # если это не последняя позиция
                            if a[lamp_name][0] == 0 and a[lamp_name][2] != 0:  # выключена и ресурс не исчерпан
                                a[lamp_name] = 1, exposure_time, a[lamp_name][2]  # лампа: (вкл, когда вкл, ресурс)
                            elif a[lamp_name][0] == 1:  # включена
                                ds = exposure_time - a[lamp_name][1]
                                if type(ds) == timedelta:
                                    ds = ds.total_seconds()
                                remaining_resource = a[lamp_name][2] - int(ds) # оставшийся ресурс = ресурс - (время воздействия - время включения этой лампы)
                                if remaining_resource > 0:  # лампа не сгорела
                                    a[lamp_name] = 0, 0, remaining_resource  # лампа: (выкл, когда вкл, ресурс)
                                else:  # сгорела
                                    a[lamp_name] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                        else:  # последняя позиция
                            if a[lamp_name][0] == 1:  # если данная лампа выключается
                                a[lamp_name] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                if 1 in lamps_condition:  # есть включенные лампы
                                    lighting_duration_1 = 0  # для операций сравнения какая лампа просветилась дольше
                                    for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                        if (a[switched_on][0] == 1) and (a[switched_on][1] + timedelta(seconds=a[switched_on][2]) > start_watching):  # если эта лампа включена, и она способна просветится до момента подачи питания на датчик
                                            if a[switched_on][1] + timedelta(seconds=a[switched_on][2]) > end_watching:  # если она даже перебежала за момент снятия питания с датчика
                                                lighting_duration_1 = int((end_watching - start_watching).total_seconds())  # выдать в результат как ввесь наблюдаемый промежуток было освещено
                                            else:  # до финиша не до жила
                                                lighting_duration_2 = (a[switched_on][1] + timedelta(seconds=a[switched_on][2])) - start_watching  # кусок времени после подачи питания на датчик
                                                lighting_duration_2 = int(lighting_duration_2.total_seconds())
                                                if lighting_duration_2 > lighting_duration_1:  # если эта лампа проработала дольше
                                                    lighting_duration_1 = lighting_duration_2
                                    return lighting_duration_1
                    elif exposure_time == start_watching:  # если воздействие попадет так что оно совпадает с подачей питания на датчик
                        if i != len(els) - 1:  # если это не последняя позиция
                            if a[lamp_name][0] == 0:  # если лампа выключена, до моента обращния к кнопке
                                if a[lamp_name][2] != 0:  # если ресурс лампы не исчерпан
                                    a[lamp_name] = 1, exposure_time, a[lamp_name][2]  # лампа: (вкл, когда вкл, ресурс)
                                    light_sensor = exposure_time  # подача питания на датчик и включение лампы совпали, датчик сразуже начал это регистрировать
                                else:  # ресурс лампы исчерпан
                                    if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                        for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                            if a[switched_on][0] == 1:  # если эта лампа включена
                                                moment_before = exposure_time - a[switched_on][1]  # сколько просветилась до этой позиции (поз - когда вкл)
                                                remaining_resource = a[switched_on][2] - moment_before.second  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                                if remaining_resource > 0:  # если ресурс лампы еще остался значит досветилась
                                                    light_sensor = exposure_time  # было подано питание на датчик, он сразуже начал это регистрировать
                                                    break  # прервать этот цикл
                                                else:  # лампа сдохла, вырубим ее в словаре
                                                    a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                            else:  # лампа включена до момента обращения к ней
                                ds = exposure_time - a[lamp_name][1]  # (время воздействия) - (время включения этой лампы)
                                if type(ds) == timedelta:  # если здесь тип timedelta
                                    ds = ds.total_seconds()  # преобразовать в секунды таким способом
                                remaining_resource = a[lamp_name][2] - int(ds)  # (оставшийся ресурс) = (ресурс) - (время работы до воздействия)
                                if remaining_resource > 0:  # лампа еще жива
                                    a[lamp_name] = 0, 0, remaining_resource  # лампа: (выкл, когда вкл, ресурс)
                                else:  # сгорела
                                    a[lamp_name] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                    for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                        if a[switched_on][0] == 1:  # если эта лампа включена
                                            moment_before = exposure_time - a[switched_on][1]  # сколько просветилась до этой позиции (поз - когда вкл)
                                            if type(moment_before) == timedelta:  # если здесь тип timedelta
                                                moment_before = int(moment_before.total_seconds())  # преобразовать в секунды таким способом
                                            remaining_resource = a[switched_on][2] - moment_before  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                            if remaining_resource > 0:  # если ресурс лампы еще остался значит досветилась
                                                light_sensor = exposure_time  # было подано питание на датчик, он сразуже начал это регистрировать
                                                break  # прервать этот цикл
                                            else:  # лампа сдохла, вырубим ее в словаре
                                                a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                        else:  # это воздействие последнее
                            if a[lamp_name][0] == 0:  # если лампа выключена, до моента обращния к кнопке
                                if a[lamp_name][2] != 0:  # если ресурс лампы не исчерпан
                                    max = start_watching + timedelta(seconds=a[lamp_name][2])  # солько еще лампа просветится?
                                    if max >= end_watching:  # если лампа захватила ввесь диапазон наблюдения
                                        return int((end_watching - start_watching).total_seconds())
                                    else:  # не ввесь диапазон
                                        if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                            for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                                if a[switched_on][0] == 1:  # если эта лампа включена
                                                    moment_before = exposure_time - a[switched_on][1]  # сколько просветилась до этой позиции (поз - когда вкл)
                                                    if type(moment_before) == timedelta:  # если здесь тип timedelta
                                                        moment_before = int(moment_before.total_seconds())  # преобразовать в секунды таким способом
                                                    remaining_resource = a[switched_on][2] - moment_before  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                                    if remaining_resource > 0:  # если ресурс лампы еще остался значит досветилась
                                                        if remaining_resource > light_sensor.second:  # если данная лампа просветилась дольше остальных
                                                            light_sensor = remaining_resource  # было подано питание на датчик, он сразуже начал это регистрировать
                                            return light_sensor  # выдать больше просветившуюся
                                        else:  # включенных ламп нету
                                            return a[lamp_name][2]  # выдать оставшеесь время работы лампы
                                else:  # сгорела
                                    if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                        for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                            if a[switched_on][0] == 1:  # если эта лампа включена
                                                moment_before = exposure_time - a[switched_on][1]  # сколько просветилась до этой позиции (поз - когда вкл)
                                                if type(moment_before) == timedelta:  # если здесь тип timedelta
                                                    moment_before = int(moment_before.total_seconds())  # преобразовать в секунды таким способом
                                                remaining_resource = a[switched_on][2] - moment_before  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                                if remaining_resource > 0:  # если ресурс лампы еще остался значит досветилась
                                                    if remaining_resource > light_sensor.second:  # если данная лампа просветилась дольше остальных
                                                        light_sensor = remaining_resource  # было подано питание на датчик, он сразуже начал это регистрировать
                                        return light_sensor  # выдать больше просветившуюся
                                    else:  # включенных ламп нету
                                        return a[lamp_name][2]  # выдать оставшеесь время работы лампы
                            else:  # лампа включена до момента обращения к ней (последнее воздействие, поз == старту)
                                a[lamp_name] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                    for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                        if a[switched_on][0] == 1:  # если эта лампа включена
                                            moment_before = exposure_time - a[lamp_name][1]  # сколько просветилась до этой позиции (поз - когда вкл)
                                            if type(moment_before) == timedelta:  # если здесь тип timedelta
                                                moment_before = int(moment_before.total_seconds())  # преобразовать в секунды таким способом
                                            remaining_resource = a[lamp_name][2] - moment_before  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                            if remaining_resource >= (end_watching - start_watching).total_seconds():  # проработала весь период наблюдения
                                                return int((end_watching - start_watching).total_seconds())   # вернуть время диапазона наблюдения
                                            else:  # либо не дожила к старту, либо к финишу
                                                if remaining_resource > 0:  # если ресурс лампы еще остался значит досветилась
                                                    if remaining_resource > light_sensor.second:  # если данная лампа просветилась дольше остальных
                                                        light_sensor = remaining_resource  # было подано питание на датчик, он сразуже начал это регистрировать
                                    return int(light_sensor.second)  # выдать результата наблюдений
                                else:  # включенных ламп не осталось
                                    return 0  # до наблюдения никто не досветился

                    elif start_watching < exposure_time < end_watching:  # если воздействие попадет так что оно между стартои и финишом наблюдения
                        if i != len(els) - 1:  # если это не последняя позиция
                            if a[lamp_name][0] == 0:  # если лампа выключена, до моента обращния к кнопке
                                if a[lamp_name][2] != 0:  # если ресурс лампы не исчерпан
                                    if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                        max = 0  # переменная для сравнений, какая лампа дольше просветилась в измеряемом промежутке
                                        for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                            if a[switched_on][0] == 1:  # если эта лампа включена
                                                if a[switched_on][1] < start_watching:  # если она была включена до старта наблюдения
                                                    moment_before = start_watching - a[switched_on][1]  # сколько просветилась до старта (старт - когда вкл)
                                                    remaining_resource = a[switched_on][2] - moment_before.second  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                                    if remaining_resource > 0:  # лампа дожила к наблюдению за ней
                                                        jkj = exposure_time - start_watching  # кусок  (позиция воздействия - позиця подключения датчика)
                                                        if remaining_resource >= jkj.second:  # ресурс лампы больше чем этот кусок?
                                                            a[switched_on] = 1, exposure_time, int(jkj.second - remaining_resource)  # лампа: (вкл, когда вкл, ресурс)
                                                            max = int(jkj.second)  # ввесь промежуток
                                                        else:  # ресерс не позволил лампе досветится к времени данного воздействия
                                                            a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                                            if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                                max = remaining_resource  # ресурс этой лампы
                                                    else:  # сгорела до старта наблюдения
                                                        a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                                elif start_watching <= a[switched_on][1]:  # если включена со стартом наблюдения или после него
                                                    gfd = exposure_time - a[switched_on][1]  # кусок времени от включения этой лампы до воздействия
                                                    if type(gfd) == timedelta:
                                                        gfd = gfd.total_seconds()
                                                    if a[switched_on][2] >= gfd:  # если лампа до жила к этому воздействию
                                                        if gfd > max:  # если эта лампа просветилась дольше остальных
                                                            max = int(gfd)  # время этой лампы
                                                        a[switched_on] = 1, exposure_time, a[switched_on][2] - int(gfd)  # лампа: (вкл, когда вкл, ресурс)
                                                    else:  # не дожила к воздействию
                                                        if gfd > max:  # если эта лампа просветилась дольше остальных
                                                            max = int(gfd)  # время этой лампы
                                                        a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                        lighting_duration += int(max)  # регистрация времени освещенности помещения во время наблюдения
                                    a[lamp_name] = 1, exposure_time, a[lamp_name][2]  # лампа: (вкл, когда вкл, ресурс)
                                else:  # ресурс лампы исчерпан
                                    if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                        max = 0  # переменная для сравнений, какая лампа дольше просветилась в измеряемом промежутке
                                        for switched_on in a:  # пробежка по словарю в поисках включенной лампы
                                            if a[switched_on][0] == 1:  # если эта лампа включена
                                                if a[switched_on][1] < start_watching:  # если она была включена до старта наблюдения
                                                    moment_before = start_watching - a[switched_on][1]  # сколько просветилась до старта (старт - когда вкл)
                                                    remaining_resource = a[switched_on][2] - moment_before.second  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                                    if remaining_resource > 0:  # лампа дожила к наблюдению за ней
                                                        jkj = exposure_time - start_watching  # кусок  (позиция воздействия - позиця подключения датчика)
                                                        if remaining_resource >= jkj.second:  # ресурс лампы больше чем этот кусок?
                                                            a[switched_on] = 1, exposure_time, int(jkj.second - remaining_resource)  # лампа: (вкл, когда вкл, ресурс)
                                                            max = int(jkj.second)  # ввесь промежуток
                                                        else:  # ресерс не позволил лампе досветится к времени данного воздействия
                                                            a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                                            if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                                max = remaining_resource  # ресурс этой лампы
                                                    else:  # сгорела до старта наблюдения
                                                        a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                                elif start_watching <= a[switched_on][1]:  # если включена со стартом наблюдения или после него
                                                    gfd = exposure_time - a[switched_on][1]  # кусок времени от включения этой лампы до воздействия
                                                    if a[switched_on][2] >= gfd.second:  # если лампа до жила к этому воздействию
                                                        if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                            max = int(gfd.second)  # время этой лампы
                                                        a[switched_on] = 1, exposure_time, a[switched_on][2] - int(gfd.second)  # лампа: (вкл, когда вкл, ресурс)
                                                    else:  # не дожила к воздействию
                                                        if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                            max = int(gfd.second)  # время этой лампы
                                                        a[switched_on] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                        lighting_duration += int(max)  # регистрация времени освещенности помещения во время наблюдения
                            else:  # лампа включена до момента обращения к ней
                                k_time = exposure_time - a[lamp_name][1]  # проработанное время (воздействие - когда включена)
                                if k_time >= timedelta(seconds=a[lamp_name][2]):  # если проработанное время не исчерпало ресурс лампы
                                    if a[lamp_name][1] < start_watching:  # если лампа была включена до старта наблюдения
                                        lighting_duration += int((exposure_time - start_watching).second)  # регистрация времени освещенности помещения во время наблюдения
                                    else:  # после старта подачи питания на датчик
                                        lighting_duration += int(k_time.second)  # регистрация времени освещенности помещения во время наблюдения
                                    a[lamp_name] = 0, 0, a[lamp_name][2] - int(k_time.second)  # лампа: (выкл, когда вкл, ресурс)
                                else:  # до воздействия лампа перегорела
                                    max = 0  # для сравнений между собой включенных ламп
                                    if a[lamp_name][1] < start_watching:  # если лампа была включена до старта наблюдения
                                        if a[lamp_name][1] + timedelta(seconds=a[lamp_name][2]) >= start_watching:  # до светилась ли она к старту наблюдения
                                            max = a[lamp_name][2] - int((start_watching - a[lamp_name][1]).second)  # ресурс - (старт - вкл)
                                    else:  # включена после активации наблюдения
                                        max = a[lamp_name][2]  # ресурс
                                    a[lamp_name] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                    if 1 in lamps_condition:  # если есть включенные лампы, дожили ли они к этому времени
                                        for HD in a:  # в поисках включенных ламп
                                            if a[HD][0] == 1:  # если эта лампа включена
                                                if a[HD][1] < start_watching:  # если она была включена до старта наблюдения
                                                    moment_before = start_watching - a[HD][1]  # сколько просветилась до старта (старт - когда вкл)
                                                    remaining_resource = a[HD][2] - moment_before.second  # оставшийся ресурс лампы (ресурс - уже просветилась)
                                                    if remaining_resource > 0:  # лампа дожила к наблюдению за ней
                                                        jkj = exposure_time - start_watching  # кусок  (позиция воздействия - позиця подключения датчика)
                                                        if remaining_resource >= jkj.second:  # ресурс лампы больше чем этот кусок?
                                                            a[HD] = 1, exposure_time, int(remaining_resource - jkj.second)  # лампа: (вкл, когда вкл, ресурс)
                                                            max = int(jkj.second)  # ввесь промежуток
                                                        else:  # ресерс не позволил лампе досветится к времени данного воздействия
                                                            a[HD] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                                            if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                                max = remaining_resource  # ресурс этой лампы
                                                    else:  # сгорела до старта наблюдения
                                                        a[HD] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                                elif start_watching <= a[HD][1]:  # если включена со стартом наблюдения или после него
                                                    gfd = exposure_time - a[HD][1]  # кусок времени от включения этой лампы до воздействия
                                                    if a[HD][2] >= gfd.second:  # если лампа до жила к этому воздействию
                                                        if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                            max = int(gfd.second)  # время этой лампы
                                                        a[HD] = 1, exposure_time, a[HD][2] - int(gfd.second)  # лампа: (вкл, когда вкл, ресурс)
                                                    else:  # не дожила к воздействию
                                                        if remaining_resource > max:  # если эта лампа просветилась дольше остальных
                                                            max = int(gfd.second)  # время этой лампы
                                                        a[HD] = 0, 0, 0  # лампа: (выкл, когда вкл, ресурс)
                                        lighting_duration += int(max)  # регистрация времени освещенности помещения во время наблюдения
                        else:  # это воздействие последнее
                            if a[lamp_name][0] == 0: # лампа на которую припало воздействия будет (включена) или выключена?
                                if a[lamp_name][2] > 0:  # если лампа не сдохла
                                    a[lamp_name] = 1, exposure_time, a[lamp_name][2]  # лампа: (вкл, когда вкл, ресурс)
                            else:  # лампа на которую припало воздействия будет включена или (выключена)?
                                # досветилась ли она к воздействию на нее?
                                ttre = exposure_time - a[lamp_name][1]  #  сколько должна была работать (воздействие - включили)
                                if a[lamp_name][2] >= ttre.second:  # если ресурса у лампы более или равно должной работе до воздействия
                                    # если лампа была включена до подачи питания на датчик
                                    # если лампа была включена с подачей питания на датчик, или после нее
                            # теперь проверить все включенные лампы
                            for three in a:  # пробежка по словарю в поисках включенных ламп
                                # если лампа включена


                return lighting_duration









if __name__ == '__main__':
    print("Пример:")
    print(sum_light([(datetime(2015, 1, 12, 10, 2, 5), 50), (datetime(2015, 1, 12, 10, 2, 7), 3),
                     (datetime(2015, 1, 12, 10, 2, 10), 50), (datetime(2015, 1, 12, 10, 2, 10), 50)], start_watching=datetime(2015, 1, 12, 10, 2, 10),
                    end_watching=datetime(2015, 1, 12, 10, 2, 30), operating=timedelta(seconds=20)), "<=== 17", "вариант когда, все действия закончились в момент подачи питаниея на датчик")
    print(sum_light([(datetime(2015, 1, 12, 10, 2, 5), 50), (datetime(2015, 1, 12, 10, 2, 7), 3),
                     (datetime(2015, 1, 12, 10, 2, 9), 50)], start_watching=datetime(2015, 1, 12, 10, 2, 10),
                    end_watching=datetime(2015, 1, 12, 10, 2, 30), operating=timedelta(seconds=20)), "<=== 17", "вариант когда, все действия произошли до подачи питания на датчик")



    print(sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                     (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                    start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
                    operating=timedelta(seconds=20)), "<=== 20")

    print(sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                     (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                     datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                     (datetime(2015, 1, 12, 10, 1, 20), 2), (datetime(2015, 1, 12, 10, 1, 40), 2)],
                    start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)), "<=== 50")
    print(sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                     (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2),
                     datetime(2015, 1, 12, 10, 0, 40), (datetime(2015, 1, 12, 10, 0, 50), 2),
                     (datetime(2015, 1, 12, 10, 1, 0), 3), (datetime(2015, 1, 12, 10, 1, 20), 3)],
                    operating=timedelta(seconds=10)), "<=== 30")
    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30),
                     (datetime(2015, 1, 12, 10, 0, 30), 2), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                    operating=timedelta(seconds=20)), "<=== 40")
    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                     datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)],
                    operating=timedelta(seconds=100)), "<=== 60")
    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)],
                    operating=timedelta(seconds=5)), "<=== 5")
    print(sum_light([(datetime(2015, 1, 12, 10, 0, 10), 3), datetime(2015, 1, 12, 10, 0, 20),
                     (datetime(2015, 1, 12, 10, 0, 30), 3), (datetime(2015, 1, 12, 10, 0, 30), 2)],
                    start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
                    operating=timedelta(seconds=5)), "<=== 10")

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
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), (datetime(2015, 1, 12, 10, 0, 0), 2),
                      datetime(2015, 1, 12, 10, 0, 10), (datetime(2015, 1, 12, 10, 1, 0), 2)],
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