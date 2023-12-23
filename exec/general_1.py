#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def average_geo(*args):
    """
    Функция для рассчёта среднего геометрического значения
    введённых чисел. Если числа отсутствуют, то функция
    вернёт None
    """
    
    if args:
        list = [int(arg) for arg in args]
        result = 1

        for value in list:
            result *= value

        return result**(1 / len(list))

    else:
        return None


if __name__ == "__main__":
    arg_list = input("Введите несколько значений: ").split()
    print(f"Результат вывода: {average_geo(*arg_list)}")
