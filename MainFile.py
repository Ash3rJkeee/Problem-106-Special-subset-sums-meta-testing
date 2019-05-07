"""Условие задачи http://euler.jakumo.org/problems/view/106.html"""

import itertools

a4 = [3, 5, 6, 7]

combinations = set()
pair_combinations = list()

for i in range(1, len(a4)):
    combinations.update(itertools.combinations(a4, i))


combinations = list(combinations)
combinations.sort()
num = 0

for i in combinations:
    b_ = list(combinations)
    b_.remove(i)
    for j in b_:
        sum_i = sum(i)
        sum_j = sum(j)
        len_set_i = len(list(i))
        len_set_j = len(list(j))

        set_i = set(i)
        set_j = set(j)

        # определяем непересекающиеся подмножества и проводим над ними проверку по условию
        if set_i.isdisjoint(set_j):
            if len_set_j == len_set_i:
                # проверка, чтобы не дублировать пары
                if [j, i] not in pair_combinations:
                    pair_combinations.append([i, j])

num = 0
for i in pair_combinations:
    print(num, i)
    num = num + 1
