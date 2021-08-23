from itertools import starmap
from sympy.geometry import Point, Polygon, are_similar


def poly(points):  # подпрога, генирирующая инфу для сравнения объектов
    return Polygon(*starmap(Point, points))  # многоугольник(точки)


def similar_triangles(coords_1, coords_2):  # основная программа
    return are_similar(poly(coords_1), poly(coords_2))  # Сходны два геометрических объекта? (вызывая продпргу)


if __name__ == '__main__':
    print("Пример:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))  # True
    print(similar_triangles([(-2, 1), (3, -2), (-3, 1)], [(6, -4), (-9, 5), (9, -4)]))  # True

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'базовый'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'другой # 1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'масштабирование'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'отражение'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'масштабирование и отражение'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'другой # 2'
    assert similar_triangles([(-2, 1), (3, -2), (-3, 1)], [(6, -4), (-9, 5), (9, -4)]) is True, "доп роверочный варик"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")

    """ мое первое решение данной задачи
    from typing import List, Tuple
    Coords = List[Tuple[int, int]]
    import math
        def hypotenuse(a, b):  # поиск длины отрезка, как будто это гипотенуза
            from math import sqrt  # чтобы воспользоватся квадратным корнем
            x = b[0] - a[0]  # отрезок по иксу
            y = b[1] - a[1]  # отрезок по игрику
            return sqrt((x ** 2) + (y ** 2))  # отдать длину стороны

        def angle(coords: Coords):  # углы треугольника
            ab1 = hypotenuse(coords[0], coords[1])  # длина отрезка между точками "a" и "b"
            bc1 = hypotenuse(coords[1], coords[2])  # длина отрезка между точками "b" и "c"
            ca1 = hypotenuse(coords[0], coords[2])  # длина отрезка между точками "c" и "a"
            cosa = math.degrees(math.acos(((ab1 ** 2) + (ca1 ** 2) - (bc1 ** 2)) / (2 * ab1 * ca1)))  # с радиан в градусы
            cosb = math.degrees(math.acos(((ab1 ** 2) + (bc1 ** 2) - (ca1 ** 2)) / (2 * ab1 * bc1)))  # с радиан в градусы
            cosc = math.degrees(math.acos(((bc1 ** 2) + (ca1 ** 2) - (ab1 ** 2)) / (2 * ca1 * bc1)))  # с радиан в градусы
            return [float('{:.2f}'.format(cosa)), float('{:.2f}'.format(cosb)), float('{:.2f}'.format(cosc))]  # отдать список углов, с двумя символами после запятой

        a = sorted(angle(coords_1))  # получение списка углов первого треугольника, + сортировка
        b = sorted(angle(coords_2))  # получение списка углов второго треугольника, + сортировка
        if a == b:  # если треугольники единтичны или маштабированы, не отраженные и не повернутые
            return True  # идентичность зафиксирована
        else:  # треугольники чуток не похожи, пожет отражение или поворот
            return False  # разные
    """