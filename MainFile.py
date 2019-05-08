"""Условие задачи http://euler.jakumo.org/problems/view/106.html"""

import itertools

a = [3, 5, 6, 7]

combinations = set()
pair_combinations = list()

for b in range(1, len(a)):
    combinations.update(itertools.combinations(a, b))


combinations = list(combinations)
combinations.sort()
num = 0

for b in combinations:
    b_ = list(combinations)
    b_.remove(b)
    for с in b_:
        sum_i = sum(b)
        sum_j = sum(с)
        len_set_b = len(list(b))
        len_set_c = len(list(с))

        set_b = set(b)
        set_c = set(с)

        # определяем непересекающиеся подмножества и проводим над ними проверку по условию
        if set_b.isdisjoint(set_c):
            # проверка, чтобы не дублировать пары
            if [с, b] not in pair_combinations:
                if (len_set_b > 1) and (len_set_c > 1):
                    if len_set_b == len_set_c:
                        pair_combinations.append([b, с])

num = 0
for pair in pair_combinations:
    print(num, pair)
    num = num + 1


# a4 = [3, 5, 6, 7]
# a7 = [20, 31, 38, 39, 40, 42, 45]

