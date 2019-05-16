"""Условие задачи http://euler.jakumo.org/problems/view/106.html"""

# todo 1) Написать функцию проверки пар подмножеств на удовлетворение условию. ГОТОВО
# todo 2) Найти оптимальное А для n=12.
# todo 3) Переписать функцию уточнения (оптимизации) А для n=12 или для неограниченного количества n.

import itertools


def find_pairs(input):
    def pairs_comparison(b, c):
        """попарно сравнивает множества между собой"""
        if b[0] > c[0]:
            if len(b) == 1:
                return True
            for i in range(1, len(b)):
                if b[i] < c[i]:
                    return True
        if b[0] < c[0]:
            if len(b) == 1:
                return True
            for i in range(1, len(b)):
                if b[i] > c[i]:
                    return True

    a = input

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
    return pair_combinations





a = [20, 31, 38, 39, 40, 42, 45]
pair_combinations = find_pairs(a)


num = 0
for pair in pair_combinations:
    print(num, pair)
    num = num + 1


# a4 = [3, 5, 6, 7]
# a7 = [20, 31, 38, 39, 40, 42, 45]

