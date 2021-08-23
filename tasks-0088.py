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
    """
    Это вторая миссия серии с лампочками. Я буду стараться немного усложнять каждую последующую задачу.

Ты уже научился считать продолжительность горения лампочки, или как долго помещение было освещено. Теперь добавим еще один параметр - время начала подсчета.

Это значит, что лампочка продолжает включатся и выключатся, как и раньше. Но теперь, как результат работы функции, я хочу не просто знать, как долго было светло в комнате, а как долго комната была освещена, начиная с определенного момента.

Добавляется еще один аргумент –

start_watching
, и если он не передан, считаем, как и в предыдущей версии программы, за весь период.
    """
    i = 0  # счетчик
    while i < len(els) - 1:  # пока "i" меньше последней позиции
        if i == 0:  # если это начало
            a = els[i + 1] - els[i]
            i += 2  # шагнуть в перед
        else:  # продолжение
            a += els[i + 1] - els[i]
            i += 2  # шагнуть в перед
    if a.days != 0:  # если есть информация в днях
        return int((a.days * 86400) + a.seconds)  # секунд в дне на дни + оставшиеся секунды без дней
    else:  # нету данных о днях
        return int(a.seconds)  # секунд


if __name__ == '__main__':
    print("Example:")
    print(sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10)]) == 610
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10),
                      datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 12, 11, 10, 10)]) == 1220
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 10, 10),
                      datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 12, 11, 10, 10),
                      datetime(2015, 1, 12, 11, 10, 10), datetime(2015, 1, 12, 12, 10, 10)]) == 4820
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 1)]) == 1
    assert sum_light([datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10),
                      datetime(2015, 1, 12, 11, 0, 0), datetime(2015, 1, 13, 11, 0, 0)]) == 86410
    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    return 0


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 5)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 0)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 10)) == 600

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 10, 10, 0)) == 620

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 10, 11)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 9, 11)) == 60

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")