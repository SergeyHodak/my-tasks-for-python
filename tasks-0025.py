def bigger_price(limit: int, data: list) -> list:
    """
    ТОП самых дорогих товаров 
    Дана таблица всех доступных продуктов на складе.
    Данные представлены в виде списка словарей (a list of dicts)
    Ваша миссия тут - это найти ТОП самых дорогих товаров.
    Количество товаров, которые мы ищем, будет передано в первом аргументе,
    а сами данные по товарам будут переданы вторым аргументом.
    тип данных = словарь - dict
    """
    a = []  # пустой список для процессов сортировки
    for i in range(0, len(data)):  # пробежка от нуля к концу списка словарей
        a.append(data[i]["price"])  # добавить в конец значение цены с положения и
    a.sort(reverse=True)  # сортирует на убывание
    b = []  # пустой список для вывода результата
    for i in range(0, len(a)):  # пробежка от нуля к концу отсортированного списка значений
        s = 0  # флаг для вайла
        f = 0  # шагатель
        while s == 0:  # пока нет тормоза "s>0"
            if data[f]["price"] == a[i]:  # если строка "f" из списка словарей "data" своей ценой равна с позицией "i" из отсортированного списка цен "a"
                b.append(data[f])  # вносим ее в список "b" для вывода
                s = 1  # прекращаем цикл вайл
            else:  # если строка "f" из списка словарей "data" своей ценой НЕ равна с позицией "i" из отсортированного списка цен "a"
                f += 1  # повышаем шаг
    return b[0:limit]  # отдать результат согласно первого полученного аргумента функции, от до лимита


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
