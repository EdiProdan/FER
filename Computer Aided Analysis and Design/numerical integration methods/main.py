import numpy as np

from lab.lab1.Matrix import Matrix
from lab.lab5.euler import euler
from lab.lab5.backward_euler import backward_euler
from lab.lab5.trapezoidal import trapezoidal
from lab.lab5.runge_kutta import runge_kutta
from lab.lab5.pece import pece
from lab.lab5.pece2 import pece2

from lab.lab5.utils import mathematical_pendulum, plot_graphs, output_result, output_result_diff

if __name__ == "__main__":

    print("============ Exercise 1 ============")

    T = 0.1
    t_max = 10
    iter_print = 1

    x0 = Matrix(matrix=[[1], [1]])
    A = Matrix(matrix=[[0, 1], [-1, 0]])

    t_list = np.arange(0, t_max + 2 * T, T)

    pendulum = mathematical_pendulum(t_list)

    euler_res = euler(A, x0, T, t_max)
    backward_euler_res = backward_euler(A, x0, T, t_max)
    trap_res = trapezoidal(A, x0, T, t_max)
    rk_res = runge_kutta(A, x0, T, t_max)
    pece_res = pece(A, x0, T, t_max)
    pece2_res = pece2(A, x0, T, t_max)

    output_result_diff(t_list, pendulum, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "1")

    plot_graphs(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "1", pendulum)

    print("============ Exercise 2 ============")

    T = 0.1
    # T = 0.01
    t_max = 1

    x0 = Matrix(matrix=[[1], [-2]])
    A = Matrix(matrix=[[0, 1], [-200, -102]])

    euler_res = euler(A, x0, T, t_max)
    backward_euler_res = backward_euler(A, x0, T, t_max)
    trap_res = trapezoidal(A, x0, T, t_max)
    rk_res = runge_kutta(A, x0, T, t_max)
    pece_res = pece(A, x0, T, t_max)
    pece2_res = pece2(A, x0, T, t_max)

    t_list = np.arange(0, t_max + 2 * T, T)
    # t_list = np.arange(0, t_max + T, T)

    output_result(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "2")

    plot_graphs(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "2")

    print("============ Exercise 3 ============")

    T = 0.01
    t_max = 10

    x0 = Matrix(matrix=[[1], [3]])
    A = Matrix(matrix=[[0, -2], [1, -3]])
    B = Matrix(matrix=[[2, 0], [3, 0]])
    r = Matrix(matrix=[[1], [1]])

    euler_res = euler(A, x0, T, t_max, B, r)
    backward_euler_res = backward_euler(A, x0, T, t_max, B, r)
    trap_res = trapezoidal(A, x0, T, t_max, B, r)
    rk_res = runge_kutta(A, x0, T, t_max, B, r)
    pece_res = pece(A, x0, T, t_max, B, r)
    pece2_res = pece2(A, x0, T, t_max, B, r)

    t_list = np.arange(0, t_max + 2 * T, T)

    output_result(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "3")

    plot_graphs(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "3")

    print("============ Exercise 4 ============")

    T = 0.01
    t_max = 1

    x0 = Matrix(matrix=[[-1], [3]])
    A = Matrix(matrix=[[1, -5], [1, -7]])
    B = Matrix(matrix=[[5, 0], [0, 3]])
    r = Matrix(matrix=[[1], [1]])

    euler_res = euler(A, x0, T, t_max, B, r)
    backward_euler_res = backward_euler(A, x0, T, t_max, B, r)
    trap_res = trapezoidal(A, x0, T, t_max, B, r)
    rk_res = runge_kutta(A, x0, T, t_max, B, r)
    pece_res = pece(A, x0, T, t_max, B, r)
    pece2_res = pece2(A, x0, T, t_max, B, r)

    t_list = np.arange(0, t_max + T, T)

    output_result(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "4")

    plot_graphs(t_list, euler_res, backward_euler_res, trap_res, rk_res, pece_res, pece2_res, "4")
