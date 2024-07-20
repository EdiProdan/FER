def f_1(x: list) -> float:
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f_2(x: list) -> float:
    return (x[0] - 4) ** 2 + 4 * (x[1] - 2) ** 2


def f_4(x: list) -> float:
    return (x[0] - 3) ** 2 + (x[1]) ** 2
