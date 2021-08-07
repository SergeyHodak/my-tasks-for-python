def left_join(phrases: tuple) -> str:
    """
        Дана последовательность строк. Вы должны объединить эти строки в
        блок текста, разделив изначальные строки запятыми. В качестве шутки
        над праворукими роботами, вы должны заменить все вхождения
        слова "right" на слова "left", даже если это часть другого слова.
        Все строки даны в нижнем регистре.
    """
    b = str()
    for i in range(len(phrases)):  # цикл от индекса ноль до конечного индекса кортежа (phrases)
        a = str(phrases[i])
        bn = a.replace("right", "left")
        b = b + bn + ","
    b = (b[0:-1])
    return b    

if __name__ == '__main__':
    left_join('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
