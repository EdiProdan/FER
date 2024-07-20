from typing import Callable, List
from lab.lab1.Matrix import Matrix
from lab.lab2.golden_section_search import golden_section_search
from lab.lab3.utils import euclidean_norm


def newton_raphson(x_0: list, f: Callable, derivatives_list: List[Callable],
                   second_derivatives_list: List[List[Callable]], epsilon: float,
                   find_optimal_step_size: bool = False) -> tuple or None:
    x = x_0.copy()
    hessian_eval = 0
    df_eval = 0

    for _ in range(10000):

        H = Matrix(matrix=[[second_derivatives_list[0][0](x), second_derivatives_list[0][1](x)],
                           [second_derivatives_list[1][0](x), second_derivatives_list[1][1](x)]])
        hessian_eval += 1

        P, L, U = H.lu_decomposition()
        H_inverse = H.inverse(P)
        dF = Matrix(matrix=[[derivatives_list[0](x)], [derivatives_list[1](x)]])
        df_eval += 1
        delta_x = (-1) * H_inverse * dF

        if find_optimal_step_size:

            for i in range(len(x)):
                f_i = lambda x_lambda: f([x_lambda if i == j else dF[j][0] for j in range(len(x))])
                a, b = golden_section_search(x0=x[i], h=1, e=epsilon, k=0.618, f=f_i)

                step_size = (a + b) / 2
                x[i] = step_size

        else:
            for i in range(len(x)):
                x[i] += delta_x[i][0]

        df_eval += len(dF.matrix)
        if abs(euclidean_norm(dF.matrix[0])) < epsilon:
            break

        if _ == 9999 or abs(f(x)) > 10 ** 10:
            print("Does not converge.")
            return None

    return x, hessian_eval, df_eval
