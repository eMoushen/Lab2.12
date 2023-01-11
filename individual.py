#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_info(func):
    def f(*args, **kwargs):
        result = f'Площадь круга равна = {func(*args, **kwargs):1.2f}'
        return result

    return f


@print_info
def area(x):
    return 3.1415926 * x * x


if __name__ == '__main__':
    r = float(input('Введите радиус: '))
    print(area(r))
