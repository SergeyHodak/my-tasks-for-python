def is_all_upper(text: str) -> bool:
    """
    Проверьте, все ли символы в данной строке написаны заглавными буквами.
    Если строка пуста или в ней нет букв - функция должна вернуть True. 
    """
    return list(map(lambda x: x.upper(), text)) == list(text)
    # если (возвести в верхний регистр "text" в виде листа) и сравнить с
    # (преобразованной строкой в лист) получим на выходе логику правда или фальш


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
