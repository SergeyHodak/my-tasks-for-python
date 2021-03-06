from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    """
    Предварительное условие:
        Массив нажатий на кнопку всегда отсортирован по возрастанию
        В массиве нажатия кнопки нет повторяющихся элементов (значит результат всегда должен быть больше 0)
        Количество элементов всегда четное (свет со временем погаснет)
        Минимальная возможная дата - 01.01.1970.
        Максимально возможная дата 9999-12-31
    """
    i = 0  # счетчик
    while i < len(els)-1:  # пока "i" меньше последней позиции
        if i == 0:  # если это начало
            a = els[i+1] - els[i]
            i += 2  # шагнуть в перед
        else:  # продолжение
            a += els[i+1] - els[i]
            i += 2  # шагнуть в перед
    if a.days != 0:  # если есть информация в днях
        return int((a.days * 86400) + a.seconds)  # секунд в дне на дни + оставшиеся секунды без дней
    else:  # нету данных о днях
        return int(a.seconds)  # секунд


if __name__ == '__main__':
    print("Пример:")
    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10)]))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10)]) == 610
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10),
                      datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 12, 11, 10, 10)]) == 1220
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10),
                      datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 12, 11, 10, 10),
                      datetime(2015, 1, 12, 11, 10, 10), datetime(2015, 1, 12, 12, 10, 10)]) == 4820
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 1)]) == 1
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10),
                      datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 13, 11, 0, 0)]) == 86410
    print("Первая миссия серии завершена? Нажмите 'Check', чтобы получить отличные награды!")