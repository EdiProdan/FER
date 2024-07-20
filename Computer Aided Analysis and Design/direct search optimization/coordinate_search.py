from typing import Tuple

from lab.lab2.golden_section_search import golden_section_search


def coordinate_search(f, x_0: list, h: int, k: int, e: float) -> Tuple:
    x = x_0.copy()

    while True:
        xs = x.copy()
        for i in range(len(x_0)):
            x_i = x[i]
            f_i = lambda x_lambda: f([x_lambda if j == i else x[j] for j in range(len(x))])

            a, b = golden_section_search(x0=x_i, h=h, e=e, k=k, f=f_i)
            x[i] = (a + b) / 2

        if all(abs(x_i - xs_i) < e for x_i, xs_i in zip(x, xs)):
            break

    return x, f(x)
