from functions import *
from utils import config
from gradient_descent import gradient_descent
from newton_raphson import newton_raphson
from gauss_newton import gauss_newton
import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
    epsilon = config["epsilon"]

    # Exercise 1
    print("\n============ Exercise 1 ============\n")

    x_0 = config["exercise_1"]["x_0"]
    print(f"x_0 = {x_0}\n")
    print("Gradient descent with optimal step size:")
    gd_optimal = gradient_descent(x_0, f_3, f3_derivatives_list, epsilon, find_optimal_step_size=True)
    print("x* = ", gd_optimal)
    eval_count = f_3.eval_count + df_3_x_1.eval_count + df_3_x_2.eval_count
    print(f"Number of function evaluations: {eval_count}\n")
    f_3.eval_count, df_3_x_1.eval_count, df_3_x_2.eval_count = 0, 0, 0

    print("Gradient descent without optimal step size:")
    gd_without_optimal = gradient_descent(x_0, f_3, f3_derivatives_list, epsilon)
    if gd_without_optimal is not None:
        print("x* = ", gd_without_optimal)
    eval_count += f_3.eval_count + df_3_x_1.eval_count + df_3_x_2.eval_count
    f_3.eval_count, df_3_x_1.eval_count, df_3_x_2.eval_count = 0, 0, 0
    print("Number of function evaluations: ", eval_count)

    # Exercise 2
    print("\n============ Exercise 2 ============\n")
    f_1_x_0 = config["exercise_2"]["f_1_x_0"]
    f_2_x_0 = config["exercise_2"]["f_2_x_0"]

    print(f"f_1, x_0 = {f_1_x_0}\n")

    print("Gradient descent:")
    gd_optimal = gradient_descent(f_1_x_0, f_1, f1_derivatives_list, epsilon, find_optimal_step_size=True)
    if gd_optimal is not None:
        print(f"x* = {gd_optimal}")
        eval_count = f_1.eval_count + df_1_x_1.eval_count + df_1_x_2.eval_count
        print(f"Number of function evaluations: {eval_count}\n")

    f_1.eval_count, df_1_x_1.eval_count, df_1_x_2.eval_count = 0, 0, 0
    print("Newton-Raphson:")
    nr_optimal = newton_raphson(f_1_x_0, f_1, f1_derivatives_list, f1_second_derivatives_list,
                                epsilon, find_optimal_step_size=True)
    if nr_optimal is not None:
        print(f"x* = {nr_optimal[0]}")
        eval_count += f_1.eval_count + df_1_x_1.eval_count + df_1_x_2.eval_count
        print(f"Number of function evaluations: {eval_count}")
        print(f"Number of Hessians evaluations: {nr_optimal[1]}")
        print(f"Number of gradient evaluations: {nr_optimal[2]}\n")

    f_1.eval_count, df_1_x_1.eval_count, df_1_x_2.eval_count = 0, 0, 0

    print(f"f_2, x_0 = {f_2_x_0}\n")

    print("Gradient descent:")
    gd_optimal = gradient_descent(f_2_x_0, f_2, f2_derivatives_list, epsilon, find_optimal_step_size=True)
    if gd_optimal is not None:
        print(f"x* = {gd_optimal}")
    eval_count = f_2.eval_count + df_2_x_1.eval_count + df_2_x_2.eval_count
    print(f"Number of function evaluations: {eval_count}\n")
    f_2.eval_count, df_2_x_1.eval_count, df_2_x_2.eval_count = 0, 0, 0

    print("Newton-Raphson:")
    nr_optimal = newton_raphson(f_2_x_0, f_2, f2_derivatives_list, f2_second_derivatives_list,
                                epsilon, find_optimal_step_size=True)
    print(f"x* = {nr_optimal[0]}")
    eval_count += f_2.eval_count + df_2_x_1.eval_count + df_2_x_2.eval_count
    print(f"Number of function evaluations: {eval_count}")
    f_2.eval_count, df_2_x_1.eval_count, df_2_x_2.eval_count = 0, 0, 0
    print(f"Number of Hessians evaluations: {nr_optimal[1]}")
    print(f"Number of gradient evaluations: {nr_optimal[2]}\n")

    # Exercise 3
    print("\n============ Exercise 3 ============\n")

    f_4_x_0_a = config["exercise_3"]["f_4_x_0_a"]
    print(f"f_4")
    print("Newton-Raphson without optimal step size:\n")
    print(f"x_0 = {f_4_x_0_a}")

    nr_a = newton_raphson(f_4_x_0_a, f_4, f4_derivatives_list, f4_second_derivatives_list, epsilon)
    f_4_eval_count = f_4.eval_count + df_4_x_1.eval_count + df_4_x_2.eval_count
    f_4.eval_count, df_4_x_1.eval_count, df_4_x_2.eval_count = 0, 0, 0
    if nr_a is not None:
        print(f"x* = {nr_a[0]}")
        print(f"Number of function evaluations: {f_4_eval_count}")
        print(f"Number of Hessians evaluations: {nr_a[1]}")
        print(f"Number of gradient evaluations: {nr_a[2]}\n")

    f_4_x_0_b = config["exercise_3"]["f_4_x_0_b"]
    print(f"x_0 = {f_4_x_0_b}")

    nr_b = newton_raphson(f_4_x_0_b, f_4, f4_derivatives_list, f4_second_derivatives_list, epsilon)
    f_4_eval_count = f_4.eval_count + df_4_x_1.eval_count + df_4_x_2.eval_count
    f_4.eval_count, df_4_x_1.eval_count, df_4_x_2.eval_count = 0, 0, 0
    if nr_b is not None:
        print("x* = ", nr_b[0])
        print(f"Number of function evaluations: {f_4_eval_count}")
        print(f"Number of Hessians evaluations: {nr_b[1]}")
        print(f"Number of gradient evaluations: {nr_b[2]}\n")
    print()

    print("Newton-Raphson with optimal step size:\n")

    print(f"x_0 = {f_4_x_0_a}")
    nr_a = newton_raphson(f_4_x_0_a, f_4, f4_derivatives_list, f4_second_derivatives_list, epsilon,
                          find_optimal_step_size=True)
    f_4_eval_count = f_4.eval_count + df_4_x_1.eval_count + df_4_x_2.eval_count
    f_4.eval_count, df_4_x_1.eval_count, df_4_x_2.eval_count = 0, 0, 0
    print(f"x* = {nr_a[0]}")
    print(f"Number of function evaluations: {f_4_eval_count}")
    print(f"Number of Hessians evaluations: {nr_a[1]}")
    print(f"Number of gradient evaluations: {nr_a[2]}\n")

    print(f"x_0 = {f_4_x_0_b}")
    nr_b = newton_raphson(f_4_x_0_b, f_4, f4_derivatives_list, f4_second_derivatives_list, epsilon,
                          find_optimal_step_size=True)
    f_4_eval_count = f_4.eval_count + df_4_x_1.eval_count + df_4_x_2.eval_count
    f_4.eval_count, df_4_x_1.eval_count, df_4_x_2.eval_count = 0, 0, 0


    print("x* = ", nr_b[0])
    print(f"Number of function evaluations: {f_4_eval_count}")
    print(f"Number of Hessians evaluations: {nr_b[1]}")
    print(f"Number of gradient evaluations: {nr_b[2]}\n")


    # Exercise 4
    print("\n============ Exercise 4 ============\n")

    f_1_x_0 = config["exercise_2"]["f_1_x_0"]

    gn = gauss_newton(f_1_x_0, f_1, G, g_second_derivatives_list, epsilon, find_optimal_step_size=True)
    print(f"x* = {gn[0]}")
    f_1_eval_count = f_1.eval_count + df_1_x_1.eval_count + df_1_x_2.eval_count
    f_1.eval_count, df_1_x_1.eval_count, df_1_x_2.eval_count = 0, 0, 0
    print(f"Number of function evaluations: {f_1_eval_count}")
    print(f"Number of Jacobian evaluations: {gn[1]}")
    print(f"Number of non-linear equations evaluations: {gn[2]}\n")


    # Exercise 5

    print("\n============ Exercise 5 ============\n")

    x_0_a = config["exercise_5"]["x_0_a"]
    x_0_b = config["exercise_5"]["x_0_b"]
    x_0_c = config["exercise_5"]["x_0_c"]

    print(f"x_0 = {x_0_a}")
    gn = gauss_newton(x_0_a, g_5, G_exercise_5, g_second_derivatives_list_exercise_5, epsilon)
    print(f"x* = {gn[0]}\n")

    print(f"x_0 = {x_0_b}")
    gn = gauss_newton(x_0_b, g_5, G_exercise_5, g_second_derivatives_list_exercise_5, epsilon)
    print(f"x* = {gn[0]}\n")

    try:
        print(f"x_0 = {x_0_c}")
        gn = gauss_newton(x_0_c, g_5, G_exercise_5, g_second_derivatives_list_exercise_5, epsilon)
        print(f"x* = {gn}\n")
    except Exception as e:
        print(e)

    # Exercise 6

    print("\n============ Exercise 6 ============\n")

    measurements = config["exercise_6"]["measurements"]
    x_0 = config["exercise_6"]["x_0"]
    G = []
    G_derivatives = []
    for measurement in measurements:
        t = measurement[0]
        y = measurement[1]

        g = lambda x, t=t, y=y: x[0] * math.pow(math.e, x[1] * t) + x[2] - y
        dg_x_1 = lambda x, t=t, y=y: math.pow(math.e, x[1] * t)
        dg_x_2 = lambda x, t=t, y=y: x[0] * t * math.pow(math.e, x[1] * t)
        dg_x_3 = lambda x, t=t, y=y: 1
        G.append(g)
        G_derivatives.append([dg_x_1, dg_x_2, dg_x_3])

    gn = gauss_newton(x_0, f_1, G, G_derivatives, epsilon, find_optimal_step_size=False)
    print(f"x* = {gn[0]}\n")

    def M(x,t):
        return x[0] * math.pow(math.e, x[1] * t) + x[2]

    t = [measurement[0] for measurement in measurements]
    y = [measurement[1] for measurement in measurements]

    plt.plot(t, y, 'ro', label='Original data')
    plt.plot(t, [M(gn[0], t[i]) for i in range(len(t))], label='Fitted line')
    plt.legend()
    plt.savefig('plot.png')
    plt.show()
