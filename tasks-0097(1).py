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

    def on(dictionary_with_lamps):  # включение лампы при не последнем воздействии
        for lamp in dictionary_with_lamps:  # пробежка по словарю
            if dictionary_with_lamps[lamp][0] == 1:  # если лампа включена
                pass
                # воздействие - когда включена, замена время включения на время воздействия если она жива, и суммированик к наблюдению если в диапазоне

    observation_recorded = 0  # наблюдение зафиксировало (секунд освещенности помещения)
    step = 0  # номер шага
    for exposure_time, lamp in assorted_impacts:  # пробежка по воздействиям с их регистрацией влияния на освещенность помещения
        print(f"время воздействия: {exposure_time}, на лампу номер: {lamp}")
        if len(assorted_impacts)-1 > step:  # если это воздействие не последнее
            # print("зафиксировано не последний шаг", step)
            if dictionary_with_lamps[lamp][0] == 0:  # если эта лампа выключена, значит ее требуют включить этим воздействием
                #print("процедура включения лампы")
                if operating is None and start_watching is None and end_watching is None:  # здесь нету: ресурса, старта, финиша
                    if len(dictionary_with_lamps) == 1:  # если здесь только одна лампа
                        dictionary_with_lamps[lamp] = [1, exposure_time]  # лампа: вкл, когда вкл
                    else:  # не одна лампа
                        print(on(dictionary_with_lamps))



                elif operating is None and end_watching is None:  # здесь нету: ресурса, финиша
                    pass
                    dictionary_with_lamps[lamp] = [1, exposure_time]  # лампа: вкл, когда вкл
                elif operating is None and start_watching is None:  # здесь нету: ресурса, старта
                    pass
                # 4 если здесь нету: старта, финиша
                # 3 если здесь нету: ресурса
                # 2 если здесь нету: финиша
                # 1 если здесь нету: старта
                # 0 если здесь все есть
            else:  # эта лампа включена, это воздействие выключает её
                pass
                print("процедура выключения лампы")
                # 7 если здесь нету: ресурса, старта, финиша
                # 6 если здесь нету: ресурса, финиша
                # 5 если здесь нету: ресурса, старта
                # 4 если здесь нету: старта, финиша
                # 3 если здесь нету: ресурса
                # 2 если здесь нету: финиша
                # 1 если здесь нету: старта
                # 0 если здесь все есть
        else:  # воздействие последнее
            pass
            print("последнее воздействие, вынос вердиктов. шаг", step)
        step += 1  # повишение шага


print(sum_light([datetime(2015, 1, 12, 10, 1, 10), (datetime(2015, 1, 12, 10, 1, 1), 1),
                     (datetime(2015, 1, 12, 10, 1, 3), 2), datetime(2015, 1, 12, 10, 1, 4)],
                    start_watching=datetime(2015, 1, 12, 10, 1, 2), end_watching=datetime(2015, 1, 12, 10, 1, 30),
                    operating=timedelta(seconds=2)), " <=== 3")
print(sum_light([datetime(2015, 1, 12, 10, 1, 10), (datetime(2015, 1, 12, 10, 1, 1), 1),
                     (datetime(2015, 1, 12, 10, 1, 3), 2), datetime(2015, 1, 12, 10, 1, 4)]))
