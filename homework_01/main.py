"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums_list):
    """
        функция, которая принимает N целых чисел,
        и возвращает список квадратов этих чисел
        >>> power_numbers(1, 2, 5, 7)
        <<< [1, 4, 25, 49]
    """
    result = []
    for num in nums_list:
        result.append(num**2)
    return result

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
#Просто́е число́ — натуральное число, имеющее ровно два различных натуральных делителя.
#Другими словами, натуральное число p является простым, если оно отлично от 1 и делится без остатка только на 1 и на само p
#0 не является натуральным числом
#1 имеет только один делитель
    for i in range(2, num):
        #print('i=', i)
        if num % i == 0:
            break
    if i < num-1:
        return False
    else:
        return True

def filter_numbers(nums_list, flt_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if flt_type == ODD:
        return [num for num in nums_list if num % 2 != 0]

    if flt_type == EVEN:
        return [num for num in nums_list if num % 2 == 0]

    if flt_type == PRIME:
        result = []
        for num in nums_list:
            if is_prime(num):
                result.append(num)
        return result

#print(is_prime(7))
#print(filter_numbers([913, 6887, 4569, 9279, 1559, 927, 263, 6405, 3413, 6353, 4569, 2151, 4321, 4789, 161, 5501, 5787, 1053, 5147, 6667, 8695, 8435, 4347, 6101, 8911, 2353, 1891, 1705, 6017, 3017, 3639, 3045, 7093, 5959, 9791, 5505, 1489, 655, 9305, 1145], PRIME))