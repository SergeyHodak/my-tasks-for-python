def left_join(phrases: tuple) -> str:
    """
        Дана последовательность строк. Вы должны объединить эти строки в
        блок текста, разделив изначальные строки запятыми. В качестве шутки
        над праворукими роботами, вы должны заменить все вхождения
        слова "right" на слова "left", даже если это часть другого слова.
        Все строки даны в нижнем регистре.
    """
    b = str()  # пустая строка для формировки результата на вывод
    for i in range(len(phrases)):  # пробежка по кортежу (phrases)
        bn = phrases[i].replace("right", "left")  # заменяем указанную фразу другой указанной фразой 
        b += bn + ","  # записываем проверенное слово и запятую добавляем
    return b[:-1]  # выдаем результат изавившись от крайней запятой
    

if __name__ == '__main__':
    left_join('Пример:')
    print(left_join(("left", "right", "left", "stop")))
    
    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Кодирование завершено? Нажмите 'Check', чтобы просмотреть свои тесты и получить отличные награды!")
