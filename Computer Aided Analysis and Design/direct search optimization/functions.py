from math import sin, sqrt


def f_fibonacci(x):
    f_fibonacci.counter += 1
    return (x - 3) ** 2


def f(x: list) -> float:
    f.counter += 1
    return (x[0] - 3) ** 2


def f1(x: list):
    f1.counter += 1
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f2(x: list):
    f2.counter += 1
    return (x[0] - 4) ** 2 + 4 * (x[1] - 2) ** 2


def f3(x: list):
    f3.counter += 1
    return sum([(x[i] - (i + 1)) ** 2 for i in range(len(x))])


def f4(x: list):
    f4.counter += 1
    return abs((x[0] - x[1]) * (x[0] + x[1])) + (x[0] ** 2 + x[1] ** 2) ** 0.5


def f6(x: list):
    f6.counter += 1
    return 0.5 + (sin(sqrt(sum([x[i] ** 2 for i in range(len(x))]))) ** 2 - 0.5) / (
            1 + 0.001 * sum([x[i] ** 2 for i in range(len(x))])) ** 2


f_fibonacci.counter = 0
f.counter = 0
f1.counter = 0
f2.counter = 0
f3.counter = 0
f4.counter = 0
f6.counter = 0