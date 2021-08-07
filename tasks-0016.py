def is_even(num: int) -> bool:
    # your code here
    '''
    Проверить является ли число четным или нет. Ваша функция должна возвращать True если число четное, и False если число не четное.
    '''
    if num % 2 == 0: # если остаток при дилении на 2 равен 0. значит четное
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
