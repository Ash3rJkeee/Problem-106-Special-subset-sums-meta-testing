"""Условие задачи http://euler.jakumo.org/problems/view/106.html"""

import itertools
import datetime


def find_pairs(input):
    """отбирает пары подмножеств, которые необходимо проверить на равенство"""

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
        print_index = combinations.index(b)
        done = (print_index / len(combinations)) * 100
        done = round(done, 1)
        print("\r", end="")
        print("\rВыполнено " + str(done) + "%.", end="")

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


# a4 = [3, 5, 6, 7]
# a7 = [20, 31, 38, 39, 40, 42, 45]

start = datetime.datetime.now()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pair_combinations = find_pairs(a)

finish = datetime.datetime.now()
elapsed_time = finish - start


# вывод результата в консоль
num = 0
for pair in pair_combinations:
    if pair_combinations.index(pair) == 0:
        print()
    print(num, pair)
    num = num + 1

print()
print("Вычисления закончены и заняли ", elapsed_time.seconds, "секунд.")

# ответ 21384
# 394 секунды



