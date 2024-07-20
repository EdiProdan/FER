from typing import List, Tuple

from lab.lab1.Matrix import Matrix


def euler(A: Matrix, x0: Matrix, T: float, t_max: int, B: Matrix = None, r: Matrix = None,
          iter_print: int = 1) -> List[Tuple[float, float]]:
    t = 0
    x = x0
    it = 0
    I = Matrix(matrix=[[1, 0], [0, 1]])
    M = I + T * A

    x_res = [(x.matrix[0][0], x.matrix[1][0])]
    while t < t_max:
        if B is not None and r is not None:
            N = T * B
            r[0][0] = t
            r[1][0] = t
            x = M * x + N * r
        else:
            x = M * x
        if it % iter_print == 0:
            x_res.append((x.matrix[0][0], x.matrix[1][0]))
        t += T
        it += 1
    return x_res
