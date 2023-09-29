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
            count_dif = 0
            for i in range(2, num-1):
                if num % 2 == 0:
                    count_dif = count_dif+1
            if count_dif == 0:
                result.append(num)
        return result

print(filter_numbers([12, 23, 30, 31, 34], PRIME))