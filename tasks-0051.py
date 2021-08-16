"""
Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата CamelCase, принятого в JavaScript (MyFunctionName) в формат, принятый в Python (my_function_name), где все буквы - маленькие, а слова соединены знаком нижнего подчеркивания "_".

Входные данные: Название функции как строка в CamelCase

Output: То же самое название, но в under_score

Предусловия :
0 < len(string) <= 100
Во входящих данных не будет чисел или пустых строк
"""
def from_camel_case(name: str) -> str:
    #replace this for solution
    return name

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")