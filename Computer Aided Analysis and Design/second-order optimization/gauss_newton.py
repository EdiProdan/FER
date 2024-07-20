from typing import Callable
from lab.lab1.Matrix import Matrix
from lab.lab2.golden_section_search import golden_section_search


def gauss_newton(x_0: list, f: Callable, g_list: list, g_second_derivatives_list, e: float,
                 find_optimal_step_size: bool = False) -> list:
    x = x_0.copy()
    jacobian_eval = 0
    g_eval = 0
    while True:

        j_matrix = []
        for i in range(len(g_list)):
            j_matrix_row = []
            for j in range(len(x_0)):
                j_matrix_row.append(g_second_derivatives_list[i][j](x))
            j_matrix.append(j_matrix_row)

        J = Matrix(matrix=j_matrix)
        jacobian_eval += 1

        g_matrix = []

        for i in range(len(g_list)):
            g_matrix.append([g_list[i](x)])

        G = Matrix(matrix=g_matrix)
        g_eval += 1
        A = ~J * J
        g = ~J * G
        g = -1 * g

        P, L, U = A.lu_decomposition()
        y = L.forward_substitution(P * g)
        delta_x = U.backward_substitution(y)

        if find_optimal_step_size:
            f_i = lambda x_lambda: f([x[j] + x_lambda * delta_x.matrix[j][0] for j in range(len(x))])
            a, b = golden_section_search(x0=0, h=1, e=e, k=0.618, f=f_i)

            step_size = (a + b) / 2
            x = [x[i] + step_size * delta_x.matrix[i][0] for i in range(len(x))]
        else:
            x = [x[i] + delta_x.matrix[i][0] for i in range(len(x))]

        if all([abs(delta_x.matrix[i][0]) < e for i in range(len(delta_x.matrix))]):
            break

    return x, jacobian_eval, g_eval
