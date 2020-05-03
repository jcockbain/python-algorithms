def climb1(n):
    if n < 3:
        return n
    return climb1(n - 1) + climb1(n - 2)


def climb2(n):
    cache = {
        0: 0,
        1: 1,
        2: 2,
    }

    for i in range(3, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


def climb3(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    for _ in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second
