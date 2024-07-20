from typing import Callable, Tuple

from tabulate import tabulate


def explore(xp: list, dx: list, f: Callable) -> list:
    n = len(xp)

    x = xp.copy()
    for i in range(n):

        p = f(x)

        x[i] += dx[i]
        n = f(x)
        if n > p:
            x[i] -= 2 * dx[i]
            n = f(x)
            if n > p:
                x[i] += dx[i]
    return x


def hooke_jeeves_method(x0: list, dx: list, e: float, f: Callable, trace: bool = False) -> Tuple:
    xp = x0.copy()
    xb = x0.copy()
    headers = ["xb", "xp", "xn", "f(xn)"]
    hooke_jeeves_data = []

    while True:
        xn = explore(xp, dx, f)
        f_xn = f(xn)
        f_xb = f(xb)

        hooke_jeeves_data.append((xb, xp, xn, f_xn))
        if f_xn < f_xb:
            xp = [2 * xn[i] - xb[i] for i in range(len(xn))]
            xb = xn.copy()
        else:
            dx = [dx[i] / 2 for i in range(len(dx))]
            xp = xb

        if all(abs(d) < e for d in dx):
            break

    if trace:
        table = tabulate(hooke_jeeves_data, headers, tablefmt="pretty")
        print(table)

    return xb, f(xb)