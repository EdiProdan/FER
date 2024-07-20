import random
from typing import Callable, Tuple

from lab.lab4.Constraints import Constraints
from lab.lab4.utils import euclidean_norm


def box(x_0: list, f: Callable, constraints: Constraints, e: float, a: float) -> list:
    n = len(x_0)

    x_0 = constraints.check_explicit_constraints(x_0)

    x_0 = constraints.check_implicit_constraints(x_0, x_0, check_x_0=True)

    x_c = x_0.copy()

    x = generate_2n_points(x_c, n, constraints)

    while True:

        h, h_2 = find_worst_indexes(x, f)

        x_h, x_h_2 = x[h], x[h_2]

        x_c = calculate_x_c(x, h)

        x_r = reflection(x_c, x_h, a)

        x_r = constraints.check_explicit_constraints(x_r)

        x_r = constraints.check_implicit_constraints(x_r, x_c)

        if f(x_r) > f(x_h_2):
            x_r = [0.5 * (x_r[i] + x_c[i]) for i in range(n)]

        x[h] = x_r

        if euclidean_norm([x_c[i] - x_h[i] for i in range(n)]) <= e:
            break

    return x_r


def reflection(x_c: list, x_h: list, a: float) -> list:
    x_r = []
    for i in range(len(x_c)):
        x_r.append((1 + a) * x_c[i] - a * x_h[i])

    return x_r


def find_worst_indexes(x: list, f: Callable) -> Tuple[int, int]:
    f_values = [f(x_i) for x_i in x]
    h = f_values.index(max(f_values))
    f_values[h] = -1
    h_2 = f_values.index(max(f_values))

    return h, h_2


def calculate_x_c(x: list, index_to_skip: int = -1) -> list:
    points_len = len(x)
    points_len_divide = points_len
    x_dimension = len(x[0])

    if index_to_skip > -1:
        points_len_divide -= 1

    x_c = []
    for i in range(x_dimension):
        sum_ = 0
        for j in range(points_len):
            if j != index_to_skip:
                sum_ += x[j][i]
        x_c.append(sum_ / points_len_divide)
    return x_c


def generate_2n_points(x_c: list, n: int, constraints: Constraints) -> list:
    x = []

    for t in range(2 * n):
        x_i = []
        for i in range(n):
            R = random.uniform(0, 1)
            x_d = constraints.explicit_constraints[i][0]
            x_g = constraints.explicit_constraints[i][1]
            x_i.append(x_d + R * (x_g - x_d))

        x_i = constraints.check_explicit_constraints(x_i)

        x_i = constraints.check_implicit_constraints(x_i, x_c)

        x.append(x_i)

        x_c = calculate_x_c(x)

    return x
