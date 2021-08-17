"""
    Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата,
    принятого в Python (my_function_name) в CamelCase, принятый в JavaScript (MyFunctionName), где первая
    буква каждого слова - большая/заглавная.
"""
def to_camel_case(name: str) -> str:
    a = str()  # пустая строка
    i = 0  # шагатель
    while i < len(name): # пробежка по имени в формате Python
        if i != 0:  # если это не перввая позиция
            if name[i] == "_":  # если нижнее подчеркивание
                a = str(a) + str(name[i+1].upper())  # записать в верхнем регистре и перед удалить нижнее подчеркивание
                i += 2  # повысить шагатель
            else:  # нет нижнего подчеркивания
                a = str(a) + str(name[i])  # записать как есть
                i += 1  # повысить шагатель
        else:  # первая позиция
            a = str(a) + str(name[0].upper())  # записать в верхнем регистре
            i += 1  # повысить шагатель
    return a  # выдать в формате "CamelCase" для JavaScript


if __name__ == '__main__':
    print("Пример:")
    print(to_camel_case('name'))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")