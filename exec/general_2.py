#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def average_harmonic(*args):
    """
    Функция вычисления среднего гармонического значения
    введённых аргументов. Выводит None, если аргументов нет
    """
    
    if args:
        harmonic = sum(1 / int(arg) for arg in args)
        return len(args) / harmonic

    else:
        return None


if __name__ == "__main__":
    arg_list = input("Введите несколько значений: ").split()
    print(f"Среднее гармоническое: {average_harmonic(*arg_list)}")
    