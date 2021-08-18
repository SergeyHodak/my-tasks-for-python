"""
    Это вторая задача по парсингу YAML. Она представляет собой следующий этап усложнения парсинга, в котором
    добавляются типы данных, такие как null и bool, а также возможность использовать кавычки в строках.
    Вот несколько примеров:
name: "Bob Dylan"
children: 6
{
  "name": "Bob Dylan",
  "children": 6
}
Как видите, строку можно задавать в кавычках. Это могут быть как двойные, так и одинарные кавычки.
name: "Bob Dylan"
children: 6
alive: false
{
  "name": "Bob Dylan",
  "alive": False,
  "children": 6
}
true и false - это ключевые слова, определяющие булевный тип.
name: "Bob Dylan"
children: 6
coding:
{
  "coding": None,
  "name": "Bob Dylan",
  "children": 6
}
Если значение не указано, то оно становится неопределенным. Также для этого есть ключевое слово null.
"""


def yaml(a):
    # значит тайво, разбить по /n потом по : и записать в словарь выдать результат
    a = sorted(a.split("\n"))  # получаем список, результат деления преносом на новую строку, +сортировка
    b = {}  # пустой словарь для вывода результата
    for i in range(0, len(a)):  # пробежка
        a[i] = a[i].replace("'", "")  # удалить одинарную лапу
        import re  # вставляем модуль re для работы с регулярными выражениями
        if re.match("[ ]+$", a[i]):  # наличие только пробелов во всей строке. [тут то что должно присутствовать]
            pass  # пропустить ход
        elif len(a[i]) == 0:  # если строка пустая
            pass  # пропустить ход
        elif ":" not in a[i]:  # если в строке нету двоеточия
            pass  # пропустить ход
        else:  # строка с данными
            c = a[i].split(":")  # разбить по двоеточию
            if '"null"' in c[1]:
                b[c[0].strip()] = 'null'  # + в словарь по (ключу, значение), удалив пробелы вначале и конце
                continue  # продолжить с начала
            elif "" == c[1] or "null" in c[1]:  # если в значении пусто или есть флаг "null"
                b[c[0].strip()] = None  # + в словарь по (ключу, значение), удалив пробелы вначале и конце
                continue  # продолжить с начала
            c[1] = c[1].replace('"', "")  # удалить двойные кавыски
            c[1] = c[1].replace('\\', '"')  # заменить косые на кавычки
            if c[1].strip().isdigit():  # если только числа, удалив пробелы вначале и конце
                b[c[0].strip()] = int(c[1].strip())  # +ключ  +инт(значение), удалив пробелы вначале и конце
            elif "false" in c[1].lower():  # если есть эта штука, снизив в нижний регистр для сравнения
                b[c[0].strip()] = False  # + в словарь по (ключу, значение), удалив пробелы вначале и конце
            else:  # если чисел нету
                b[c[0].strip()] = c[1].strip()  # + в словарь по (ключу, значение), удалив пробелы вначале и конце
    return b  # выдать результат


if __name__ == '__main__':
    print("Пример:")
    print(yaml('name: Alex\nage: 12'))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")