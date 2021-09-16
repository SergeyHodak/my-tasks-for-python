from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None, operating: Optional[timedelta] = None) -> int:
    assorted_impacts = []  # для создания отсортированного списка "els"
    for impact in els:  # пробежка по списку воздействий
        if type(impact) == tuple:  # если здесь тип tuple, тоесть указана лампа
            assorted_impacts.append([impact[0], impact[1]])  # записать в таком виде
        if type(impact) == datetime:  # если здесь тип datetime, тоесть без номера лампы
            assorted_impacts.append([impact, 0])  # записать в таком виде
    assorted_impacts = sorted(assorted_impacts)  # отсортировать воздействия от min к max по времени
    dictionary_with_lamps = {}  # словарь из ламп, содержащий в себе всю инфу о них
    for lamp in assorted_impacts:  # пробежка по лампам
        if operating != None:  # если поступаемая информация имеет задающий ресурс для ламп
            dictionary_with_lamps[lamp[1]] = [0, 0, operating]  # какая лампа: [выкл, когда вкл, ресурс]
        else:  # без ресурса. вечные
            dictionary_with_lamps[lamp[1]] = [0, 0]  # какая лампа: [выкл, когда вкл]
    print(dictionary_with_lamps)


print(sum_light([datetime(2015, 1, 12, 10, 1, 10), (datetime(2015, 1, 12, 10, 1, 1), 1),
                     (datetime(2015, 1, 12, 10, 1, 3), 2), datetime(2015, 1, 12, 10, 1, 4)],
                    start_watching=datetime(2015, 1, 12, 10, 1, 2), end_watching=datetime(2015, 1, 12, 10, 1, 30),
                    operating=timedelta(seconds=2)), " <=== 3")
