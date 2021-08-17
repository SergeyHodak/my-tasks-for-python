"""
    Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата CamelCase,
    принятого в JavaScript (MyFunctionName) в формат, принятый в Python (my_function_name), где все буквы -
    маленькие, а слова соединены знаком нижнего подчеркивания "_".
"""
def from_camel_case(name: str) -> str:
    a = str()  # пустая строка
    for i in name:  # пробежка по имени в формате "CamelCase" для JavaScript
        if i != name[0]:  # если это не перввая позиция
            if i.isupper():  # если в верхнем регистре
                a = str(a) + str("_") + str(i.lower())  # записать в нижнем регистре и перед нижнее подчеркивание
            else:  # в нижнем регистре
                a = str(a) + str(i)  # записать как есть
        else:  # первая позиция
            a = str(a) + str(name[0].lower())  # записать в нижнем регистре
    return a  # выдать в формате для Python


if __name__ == '__main__':
    print("Пример:")
    print(from_camel_case("Name"))

    # Эти "asserts" используются только для самопроверки и не требуются для автоматического тестирования.
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Кодирование завершено? Нажмите 'Check', чтобы получить отличные награды!")