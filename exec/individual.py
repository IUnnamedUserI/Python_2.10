#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def args_sum(*args):
    """
    Функция находит минимальный элемент в ряде значений
    и считает сумму элементов, находящихся после минимального.
    В случае, если значений нет, функций возвращает None
    """
    
    if args:
        min_value = min(args)
        min_index = args.index(min_value)
        result = sum(args[min_index + 1:])
        return min_index, min_value, result
    
    else:
        return None


if __name__ == "__main__":
    arg_list = tuple(map(int, input("Введите несколько значений: ").split()))
    result = args_sum(*arg_list)
    if result is None:
        print("Ошибка ввода")
    else:
        print(f"Минимальное значение - [{result[0]}] {result[1]}")
        print(f"Результат суммы - {result[2]}")
