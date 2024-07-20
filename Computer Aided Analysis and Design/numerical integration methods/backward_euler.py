from typing import Tuple, List

from lab.lab1.Matrix import Matrix


def backward_euler(A: Matrix, x0: Matrix, T: float, t_max: int, B: Matrix = None, r: Matrix = None,
                   iter_print: int = 1) -> List[Tuple[float, float]]:
    t = 0
    x = x0
    it = 0
    I = Matrix(matrix=[[1, 0], [0, 1]])
    P = (I - T * A).inverse()
    Q = P * T * B
    x_res = [(x.matrix[0][0], x.matrix[1][0])]
    while t < t_max:
        if B is not None and r is not None:
            r[0][0] = t + T
            r[1][0] = t + T
            x = P * x + Q * r
        else:
            x = P * x
        if it % iter_print == 0:
            x_res.append((x.matrix[0][0], x.matrix[1][0]))
        t += T
        it += 1
    return x_res
