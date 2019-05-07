def func(x):
    res = 0
    for i in range(x):
        print(i)
        res = res + i
    print()
    return res


print(func(4))