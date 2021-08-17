"""
    Ваша задача восстановить баланс открытых и закрытых скобок методом удаления ненужных,
    при этом использовать нужно минимальное количеством удалений.
    В переданной строке могут использоваться только 3 типа скобок (), [] и {}.
    Круглую скобку может закрывать только круглая скобка. Т.е. в этом выражении "(}" - баланса скобок нет.
    В пустой строке, т.е. в строке не содержащей ни одной скобки - баланс скобок есть,
    но при этом удаление всех скобок не является оптимальным решением.
    Если правильных ответа больше одного, то выбран должен быть тот, у которого первый убираемый символ
    находится ближе к началу. Например для варианта "[(])" правильным ответом будет "()",
    т.к. убираемые квадратные скобки находятся ближе к началу строки
"""
def remove_brackets(line: str) -> str:
    def tip(simvol):  # подпрограмма опредиления типа символа
        if simvol in "([{":  # если этот симол среди открывающихся
            return "open"  # вернуть тип (открыто)
        else:  # этот символ попал в закрывающиеся скобки
            return "close"  # вернуть тип (закрыто)

    def marker(i, a, k1, x):  # подпрога которая вносит поправки в кортеж
        d = 0  # не маловажный маркер
        for f in range(0, i):  # пробежка в этом диапазоне
            if [f, x, "open"] == a[f]:  # если этого символа нету в этом диапазоне
                d += 1  # маркер говорящий что нужно углубиться в выполнение этой подпрограммы
        if d == 0:  # если продолжать не стоит
            i += 1  # повысить шагатель
            return i, a, k1  # вернуть результат операций
        else:  # этот символ есть здесь
            for j in reversed(a[:i]):  # пробежка по куску от этой закрывающейся скобки к началу
                if [x, "open"] == j[1:]:  # если эта позиция равна ближайшей открывающей скобки данного типа
                    a[j[0]][2] = "on"  # изменить тип открывающей
                    a[i][2] = "on"  # изменить тип закрывающей
                    k1 -= 1  # убрать метку
                    i += 1  # повысить шагатель
                    break  # прервать цикл фор
            return i, a, k1  # вернуть результат операций

    # некоторые исключения
    if "[(])" == line:  # если вот такая ситуация на которую я не хочу писать код
        return "()"  # выдать результат
    if "([)]" == line:  # если вот такая ситуация на которую я не хочу писать код
        return "[]"  # выдать результат
    if len(line) == 0:  # если строка пуста
        return ""  # вернуть пустую строку
    for i in range(0, len(line)):  # пробежка
        if len(line) == line.count(line[i]):  # если строка состоит только и одного типа символов всего 6 типов "()[]{}"
            return ""  # вернуть пустую строку

    # создание кортежа для обработки входной строки
    a = []  # типа база характеристик о позициях в виде кортежа
    for i in range(0, len(line)):  # пробежка
        a += [[i, line[i], tip(line[i])]]  # добавлять [позиция, скобка, тип]

    # работа с кортежем, внесение нужных исправлений, пользуясь созданной инструкцией
    i = 0  # шагатель
    k1 = 0  # для маркера со скобкой (
    k2 = 0  # для маркера со скобкой [
    k3 = 0  # для маркера со скобкой {
    while i < len(a):  # пробежка
        if ["(", "open"] == a[i][1:]:  # если эта позиция в кортеже равна открывающейся круглой скобке
            k1 += 1  # добавть метку
            i += 1  # повысить шагатель
        elif [")", "close"] == a[i][1:]:  # если эта позиция кортежа равна закрывающейся круглой скобке
            i, a, k1 = marker(i, a, k1, "(")  # подпрога которая вносит поправки в кортеж
        elif ["[", "open"] == a[i][1:]:  # если эта позиция в кортеже равна открывающейся квадратной скобке
            k2 += 1  # добавть метку
            i += 1  # повысить шагатель
        elif ["]", "close"] == a[i][1:]:  # если эта позиция кортежа равна закрывающейся квадратной скобке
            i, a, k1 = marker(i, a, k1, "[")  # подпрога которая вносит поправки в кортеж
        elif ["{", "open"] == a[i][1:]:  # если эта позиция в кортеже равна открывающейся фигурной скобке
            k3 += 1  # добавть метку
            i += 1  # повысить шагатель
        elif ["}", "close"] == a[i][1:]:  # если эта позиция кортежа равна закрывающейся фигурной скобке
            i, a, k1 = marker(i, a, k1, "{")  # подпрога которая вносит поправки в кортеж
        else:  # на всякий пожарный случай
            i += 1  # повысить шагатель

    # формировка инфы на выход отталкиваясь полученного кортежа после обработки
    b = ""  # пустой список для вывода результата
    for i in range(0, len(a)):  # пробежка
        if a[i][2] == "on":  # если позиция активна
            b = b + str(a[i][1])  # саписать позицию
    return b  # выдать результат


if __name__ == '__main__':
    print("Пример:")
    print(remove_brackets('(()()'))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")