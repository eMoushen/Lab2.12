#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def city(**kwargs):
    summa = 0
    n = len(kwargs)
    maxi = 0
    for kw in kwargs:
        summa += kwargs[kw]
        if kwargs[kw] > maxi:
            maxi = kwargs[kw]
    return maxi, summa/n


if __name__ == "__main__":
    print(city(
        Москва=2511,
        Петербург=515,
        Челябинск=530,
        Ростов=354
    ))
