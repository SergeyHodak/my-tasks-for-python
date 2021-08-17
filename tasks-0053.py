"""
    Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты?
    Вы можете использовать газету, чтобы рассказать кому-то свой секрет. Даже если кто-то найдет
    ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора. Один из самых
    простых способов спрятать ваше секретное сообщение это использовать заглавные буквы. Давайте
    найдем несколько таких секретных сообщений.
    Дан кусок текста.
    Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
    Например: текст = " H ow are you? E h, ok. L ow or L ower? O hhh.", если мы соберем
    все заглавные буквы, то получим сообщение "HELLO".
"""
def find_message(message: str) -> str:
    a = str()  # пустая строка
    for i in message:  # пробежка по сообщению
        if i.isupper():  # если в верхнем регистре
            a = str(a) + str(i)  # записать буковку
    return a  # выдать результат (розсекретить сообщение)


if __name__ == '__main__':
    print("Пример:")
    print(find_message(('How are you? Eh, ok. Low or Lower? ' + 'Ohhh.')))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert find_message(('How are you? Eh, ok. Low or Lower? ' + 'Ohhh.')) == 'HELLO'
    assert find_message('hello world!') == ''
    assert find_message('HELLO WORLD!!!') == 'HELLOWORLD'
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")