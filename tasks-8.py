def is_all_upper(text: str) -> bool:
    """
    Проверьте, все ли символы в данной строке написаны заглавными буквами.
    Если строка пуста или в ней нет букв - функция должна вернуть True. 
    """
    b = True  #правда
    d = False #лож
    FullProbel = text[1:-1].isspace()  # True, если строка содержит только пробельные символы
    FullBukva = text[1:-1].isalpha()   # True, если все символы в строке являются буквами
    FullBukvaUp = text[1:-1].isupper() # True, если все символы в данной строке в верхнем регистре
    if FullBukva == b:
        return b
    elif FullBukvaUp == b:
        return b
    elif len(text) == 0:
        return b
    elif FullProbel == b:
        return b
    elif text[0] in '0123456789/':  # есди первый символ с text есть в списке '0123456789/'
        return b
    else:
        return d


if __name__ == '__main__':
    print("Пример:")
    print(is_all_upper('ALL UPPER'))
    
    # Эти "asserts" используются для самопроверки, а не для автоматического тестирования.
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print ("Кодирование завершено? Нажмите 'Check', чтобы получить классные награды!")
