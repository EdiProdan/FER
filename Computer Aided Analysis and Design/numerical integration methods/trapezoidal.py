from typing import List, Tuple

from lab.lab1.Matrix import Matrix


def trapezoidal(A: Matrix, x0: Matrix, T: float, t_max: int, B: Matrix = None, r: Matrix = None,
                iter_print: int = 1) -> List[Tuple[float, float]]:
    r2 = Matrix(matrix=[[0], [0]])
    t = 0
    x = x0
    it = 0
    I = Matrix(matrix=[[1, 0], [0, 1]])
    R = (I - (T / 2) * A).inverse() * (I + (T / 2) * A)
    S = (I - (T / 2) * A).inverse() * (T / 2) * B
    x_res = [(x.matrix[0][0], x.matrix[1][0])]
    while t < t_max:
        if B is not None and r is not None:
            r[0][0] = t
            r[1][0] = t
            r2[0][0] = t + T
            r2[1][0] = t + T
            x = R * x + S * (r + r2)
        else:
            x = R * x
        if it % iter_print == 0:
            x_res.append((x.matrix[0][0], x.matrix[1][0]))
        t += T
        it += 1
    return x_res
