def bigger_price(limit: int, data: list) -> list:
    """
    ТОП самых дорогих товаров.
    Дана таблица всех доступных продуктов на складе.
    Данные представлены в виде списка словарей (a list of dicts)
    Ваша миссия тут - это найти ТОП самых дорогих товаров.
    Количество товаров, которые мы ищем, будет передано в первом аргументе,
    а сами данные по товарам будут переданы вторым аргументом.
    тип данных = словарь - dict
    """
    a = []  # список для сортировки цен
    for i in range(0, len(data)):  # пробежка по ценникам
        a.append(data[i]["price"])  # записать цену
    a[::-1] = sorted(a)  # отсортитровать и поставить на убывание
    b = []  # список для выдачи результата
    for i in range(0, limit):  # пробежать limit раз
        for j in range(0, len(data)):  # пробежка по ценникам
            if str(a[i]) in str(data[j]):  # если цена a[i] есть в позиции data[j]
                b.append(data[j])  # вносим ее в список "b" для вывода
    return b  # выдать результат


if __name__ == '__main__':
    from pprint import pprint
    print('Пример:')
    pprint(bigger_price(2, [{"name": "bread", "price": 100},
                            {"name": "wine", "price": 138},
                            {"name": "meat", "price": 15},
                            {"name": "water", "price": 1}]))

    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert bigger_price(2, [{"name": "bread", "price": 100},
                            {"name": "wine", "price": 138},
                            {"name": "meat", "price": 15},
                            {"name": "water", "price": 1}]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}], "First"

    assert bigger_price(1, [{"name": "pen", "price": 5},
                            {"name": "whiteboard", "price": 170}]) == [
        {"name": "whiteboard", "price": 170}], "Second"

    print('Готово! Похоже, все в порядке. Иди и проверь это')
