from typing import List, Tuple

from lab.lab1.Matrix import Matrix


def runge_kutta(A: Matrix, x0: Matrix, T: float, t_max: int, B: Matrix = None, r: Matrix = None,
                iter_print: int = 1) -> List[Tuple[float, float]]:
    r2 = Matrix(matrix=[[0], [0]])
    r3 = Matrix(matrix=[[0], [0]])
    t = 0
    x = x0
    it = 0
    I = Matrix(matrix=[[1, 0], [0, 1]])
    x_res = [(x.matrix[0][0], x.matrix[1][0])]
    P = I + A * T + (1 / 2) * A * A * (T * T) + (1 / 6) * A * A * A * (T * T * T) + (
                1 / 24) * A * A * A * A * (T * T * T * T)
    Q = I + A * T + (1 / 2) * A * A * (T * T) + (1 / 4) * A * A * A * (T * T * T)
    S = 4 * I + 2 * A * T + (1 / 2) * A * A * (T * T)
    while t < t_max:
        if B is not None and r is not None:
            r[0][0] = t
            r[1][0] = t
            r2[0][0] = t + T
            r2[1][0] = t + T
            r3[0][0] = t + T / 2
            r3[1][0] = t + T / 2
            x = P * x + (T / 6) * Q * B * r + (T / 6) * S * B * r3 + (T / 6) * B * r2
        else:
            x = P * x
        if it % iter_print == 0:
            x_res.append((x.matrix[0][0], x.matrix[1][0]))
        t += T
        it += 1

    return x_res
