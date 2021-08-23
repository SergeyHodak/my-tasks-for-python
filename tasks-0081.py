def unix_match(filename: str, pattern: str) -> bool:
    """
    Ваша задача - определить, соответствует ли заданное имя файла заданному поисковому паттерну.
    Вот небольшая таблица, которая показывает, какие символы могут использовать в паттернах.
        * соответствует всему (любому количеству любых символов)
        ? соответствует любому одному символу
    """
    if pattern == '*':  # еслти во втором аргументе просто звезда
        return True  # все ок
    elif filename == pattern:  # имя файла равно паттерну
        return True  # все ок
    else:  # другие варианты
        a = str()
        if "?" in pattern and "*" in pattern:  # если и вопрос и звезда присутствуют в паттерне
            for i in range(0, len(filename)):
                if len(pattern) > (len(filename) - i):  # если симвосов в паттерне больше чем символов в имени файла с учетом позиции "i"
                    return False  # все плохо
                for j in range(0, len(pattern)):  # пробежка длинной в паттерн по имени файла
                    if pattern[j] == "?":  # если эта позицция равна вопросику
                        a += str("?")  # запишем вопросик
                    elif pattern[j] == "*":  # если эта позицция равна звездочке
                        a += str("*")  # запишем звездочку
                    else:  # нету вопросика в данной позиции
                        a += str(filename[i + j])
                if a == pattern:  # если этот участок равен
                    return True  # все ок
            return False  # все плохо
        if "?" in pattern:  # если в паттерне присутствует символ вопросса
            for i in range(0, len(filename)):  # пробежка по имени файла
                if len(pattern) > (len(filename) - i):  # если симвосов в паттерне больше чем символов в имени файла с учетом позиции "i"
                    return False  # все плохо
                for j in range(0, len(pattern)):  # пробежка длинной в паттерн по имени файла
                    if pattern[j] == "?":  # если эта позицция равна вопросику
                        a += str("?")  # запишем вопросик
                    else:  # нету вопросика в данной позиции
                        a += str(filename[i + j])
                if a == pattern:  # если этот участок равен
                    return True  # все ок
            return False  # все плохо
        if "*" in pattern:  # если в паттерне присутствует символ звездочки
            pattern = pattern.replace('*', '')  # удалить все звездочки
            if pattern in filename:  # если есть такой паттерн в имени файла
                return True  # все ок
        return False  # все плохо


if __name__ == '__main__':
    print("Пример:")
    print(unix_match('somefile.txt', '*'))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    assert unix_match("l.txt", "???*") == True
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")