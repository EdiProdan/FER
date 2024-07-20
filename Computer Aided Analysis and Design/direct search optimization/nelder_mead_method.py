from typing import Tuple, Callable

from tabulate import tabulate


def generate_simplex(x0: list, h: float) -> list:
    simplex = [x0]
    for i in range(len(x0)):
        x = x0.copy()
        x[i] += h
        simplex.append(x)

    return simplex


def find_centroid(simplex: list, h: int) -> list:
    centroid = [0.0] * len(simplex[0])
    n = len(simplex) - 1

    for i, point in enumerate(simplex):
        if i != h:
            for j, coord in enumerate(point):
                centroid[j] += coord
    xc = [coord / n for coord in centroid]
    return xc


def reflection(xc: list, xh: list, alpha: float) -> list:
    xr = []
    for i in range(len(xc)):
        xr.append((1 + alpha) * xc[i] - alpha * xh[i])

    return xr


def expansion(xc: list, xr: list, gamma: float) -> list:
    xe = []
    for i in range(len(xc)):
        xe.append((1 - gamma) * xc[i] + gamma * xr[i])

    return xe


def contraction(xc: list, xh: list, beta: float) -> list:
    xk = []
    for i in range(len(xc)):
        xk.append(beta * xh[i] + (1 - beta) * xc[i])

    return xk


def shrink(simplex: list, l: int, sigma: float) -> list:
    for i, point in enumerate(simplex):
        if i != l:
            for j, coord in enumerate(point):
                simplex[i][j] = (simplex[i][j] + simplex[l][j]) * sigma
    return simplex


def nelder_mead_method(x0: list, step: float, alpha: float, beta: float, gamma: float, sigma: float, epsilon: float,
                       f: Callable, trace: bool = False) -> Tuple:
    headers = ["x_centroid", "f(x_centroid)"]
    nelder_mead_data = []
    simplex = generate_simplex(x0, step)

    while True:
        f_values = [f(x) for x in simplex]
        h = f_values.index(max(f_values))
        l = f_values.index(min(f_values))

        xc = find_centroid(simplex, h)

        nelder_mead_data.append((xc, f(xc)))
        xr = reflection(xc, simplex[h], alpha)
        f_xr = f(xr)
        f_simplex_l = f(simplex[l])
        if f_xr < f_simplex_l:
            xe = expansion(xc, xr, gamma)
            f_xe = f(xe)
            if f_xe < f_simplex_l:
                simplex[h] = xe
            else:
                simplex[h] = xr
        else:
            if all(f_xr > f(simplex[j]) for j in range(len(simplex)) if j != h):
                f_simplex_h = f(simplex[h])
                if f_xr < f_simplex_h:
                    simplex[h] = xr
                xk = contraction(xc, simplex[h], beta)
                f_xk = f(xk)
                if f_xk < f_simplex_h:
                    simplex[h] = xk
                else:
                    simplex = shrink(simplex, l, sigma)
            else:
                simplex[h] = xr
        if abs(f(simplex[l]) - f(simplex[h])) < epsilon:
            break

    if trace:
        table = tabulate(nelder_mead_data, headers, tablefmt="pretty")
        print(table)

    return simplex[l], f(simplex[l])
