"""Условие задачи http://euler.jakumo.org/problems/view/106.html"""

import itertools


def pairs_comparison(b, c):
    """попарно сравнивает множества между собой"""
    if b[0] > c[0]:
        if len(b) == 2:
            return True
        if c[-1] < b[0]:
            return False
        for i in range(1, len(b)):
            if b[i] < c[i]:
                return False
    if b[0] < c[0]:
        if len(b) == 1:
            return True
        if c[-1] > b[0]:
            return False
        for i in range(1, len(b)):
            if b[i] > c[i]:
                return False
    return True


a = [20, 31, 38, 39, 40, 42, 45]

combinations = set()
pair_combinations = list()

for b in range(1, len(a)):
    combinations.update(itertools.combinations(a, b))


combinations = list(combinations)
combinations.sort()
num = 0

for b in combinations:
    c_ = list(combinations)
    c_.remove(b)
    for c in c_:
        sum_i = sum(b)
        sum_j = sum(c)
        len_set_b = len(list(b))
        len_set_c = len(list(c))

        set_b = set(b)
        set_c = set(c)

        # определяем непересекающиеся подмножества и проводим над ними проверку по условию
        if set_b.isdisjoint(set_c):
            # проверка, чтобы не дублировать пары
            if [c, b] not in pair_combinations:
                if (len_set_b > 1) and (len_set_c > 1):
                    if len_set_b == len_set_c:
                        if pairs_comparison(b, c):
                            pair_combinations.append([b, c])

num = 0
for pair in pair_combinations:
    print(num, pair)
    num = num + 1


# a4 = [3, 5, 6, 7]
# a7 = [20, 31, 38, 39, 40, 42, 45]

