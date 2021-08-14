from typing import Union


def sun_angle(time: str) -> Union[int, str]:  # вот эта добавка говорит выплюнь либо int либо str данные
    """
    Ваша задача - определить угол солнца над горизонтом, зная время суток.
    Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0
    градусов. В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00
    солнце садится за горизонт и угол равен 180 градусов. В случае, если указано
    ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу
    "I don't see the sun!".
    ВЫДАТЬ Угол наклона солнца, округленный до двух знаков после запятой.
    """
    # 12 часов = 720 минут. 180 градусов = 12 часам.
    a = int(time[0:2])*60 + int(time[3:])  # время в минутах
    if 360 <= a <= 1080:  # если время в промежетки когда солнце видно
        return (180/720) * (a-360)  # в одной минуте градусов * минуты - после шести утра = градусы
    else:  # время за промежудком видимости солнца
        return "I don't see the sun!"  # выдать: "Я не вижу солнца!"


if __name__ == '__main__':
    print("Пример:")
    print(sun_angle("12:00"))

    # Эти "assert" используются только для самопроверки и не требуются для автоматического тестирования.
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")