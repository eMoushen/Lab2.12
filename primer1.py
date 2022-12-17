#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(func):
    def g(txt, chars=' !?'):
        tmp = ''
        for sym in func(txt):
            if sym in chars:
                sym = '-'
            tmp += sym
        while '--' in tmp:
            tmp = tmp.replace('--', '-')
        return tmp

    return g


@f
def h(txt):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

    n_str = ''
    for sym in txt.lower():
        n_str += t.get(sym, sym)

    return n_str


if __name__ == '__main__':
    txt = 'Функция должна возвращать преобразованную строку'
    print(h(txt, chars='?!:;,. '))
