from typing import Callable, List

from lab.lab2.golden_section_search import golden_section_search
from lab.lab3.utils import euclidean_norm


def gradient_descent(x_0: List[float], f: Callable, derivatives_list: List[Callable], epsilon: float,
                     find_optimal_step_size: bool = False) -> List[float] or None:
    x = x_0.copy()
    n = len(x)

    for _ in range(10000):
        gradient = [derivatives_list[i](x) for i in range(n)]
        # print(f"Gradient: {gradient}")

        if find_optimal_step_size:
            f_i = lambda x_lambda: f([x[j] - x_lambda * gradient[j] for j in range(len(x))])
            # print("X: ", x)
            for i in range(n):

                a, b = golden_section_search(x0=0, h=1, e=epsilon, k=0.618, f=f_i)

                step_size = (a + b) / 2

                x[i] -= step_size*gradient[i]
            # print("X+1: ",x)

        else:
            for i in range(n):
                x[i] -= gradient[i]

        if abs(euclidean_norm(gradient)) < epsilon:
            break

        if abs(f(x)) > 10 ** 10 or _ == 9999:
            print("Does not converge.")
            return None

    return x
