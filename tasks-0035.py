def date_time(time: str) -> str:
    """
    Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
    Люди предпочитают видеть эту же информацию в более развернутом виде:
    21 May 2018 year, 16 hours 30 minutes
    Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
    Предусловия :
        0 < date <= 31
        0 < month <= 12
        0 < year <= 3000
        0 < hours < 24
        0 < minutes < 60
    # Обратите внимание, что слова "hour" и "minute" (в единственном числе)
        используются только когда время 01:mm (1 hour) или hh:01 (1 minute).
    # Во всех остальных случаях следует использовать "hours" и "minutes".
    # Для названий месяцев и остальных слов следует использовать их английские
        эквиваленты -
        # January, February, March, April, May, June, July,
        # August, September, October, November, December;
        # year, hour/hours, minute/minutes
    """
    a = ["0", "January", "February", "March", "April", "May", "June", "July", "August", "September",
         "October", "November", "December"]  # список месяцев по их номеру
    b = time.split(" ")  # разделить по пробелу 1 и 2
    e = b[0].split(".") + b[1].split(":")  # собрать в список, разделив по точке и по двоеточию
    d = str(str(int(e[0])) + " " + str(a[int(e[1])]) + " " + str(e[2]) + " year")  # нулевой e[0] без изменений, e[1] месяц словом
    if int(e[3]) == 1:  # если час == 1
        d += str(" 1 hour")  # назвать его час, а не часа или часов. (не множественная форма)
    else:  # если значение часа более одного
        d += " " + (str(int(e[3])) + " hours")  # сколько часов + назвать в множественной форме
    if int(e[4]) == 1:  # если одна минута
        d += " 1 minute"  # назвать в одиночной форме
    else:  # если минут более одной
        d += " " + str(int(e[4])) + " minutes"  # сколько + назвать в множественной форме
    return d  # выплюнуть результат


if __name__ == '__main__':
    print("Пример:")
    print(date_time('01.01.2000 00:00'))

    # Эти "assert" используются только для самопроверки и не требуются для автоматического тестирования.
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")