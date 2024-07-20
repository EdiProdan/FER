from typing import List, Tuple

import tabulate
import matplotlib.pyplot as plt
import numpy as np


def mathematical_pendulum(t: np.ndarray) -> List[Tuple[float, float]]:
    x_1 = np.cos(t) + np.sin(t)
    x_2 = -np.sin(t) + np.cos(t)

    return list(zip(x_1, x_2))


def output_result_diff(time, mathematical_pendulum_res, euler_res, backward_euler_res, trapezoidal_res, runge_kutta_res,
                  pece_res, pece2_res, exercise, print_step=1):
    tabulate_1 = [["t", "Euler", "Backward Euler", "Trapezoidal", "Runge-Kutta", "PE(CE)", "PE(CE)2"]]
    for i, (t, analytic, euler, backward_euler, trapezoidal, runge_kutta, pece, pece2) in enumerate(
            zip(time, mathematical_pendulum_res, euler_res, backward_euler_res, trapezoidal_res, runge_kutta_res,
                pece_res, pece2_res)):
        if i % print_step == 0:
            euler_err = abs(analytic[0] - euler[0]), abs(analytic[1] - euler[1])
            backward_euler_err = abs(analytic[0] - backward_euler[0]), abs(analytic[1] - backward_euler[1])
            trapezoidal_err = abs(analytic[0] - trapezoidal[0]), abs(analytic[1] - trapezoidal[1])
            runge_kutta_err = abs(analytic[0] - runge_kutta[0]), abs(analytic[1] - runge_kutta[1])
            pece_err = abs(analytic[0] - pece[0]), abs(analytic[1] - pece[1])
            pece2_err = abs(analytic[0] - pece2[0]), abs(analytic[1] - pece2[1])
            tabulate_1.append([t, euler_err, backward_euler_err, trapezoidal_err, runge_kutta_err, pece_err, pece2_err])

    with open("results/" + exercise + ".txt", "w") as f:
        f.write(tabulate.tabulate(tabulate_1, headers="firstrow", tablefmt="fancy_grid"))


def output_result(time, euler_res, backward_euler_res, trapezoidal_res, runge_kutta_res,
                  pece_res, pece2_res, exercise, print_step=1):
    tab = [["t", "Euler", "Backward Euler", "Trapezoidal", "Runge-Kutta", "PE(CE)", "PE(CE)2"]]
    for i, (t, euler, backward_euler, trapezoidal, runge_kutta, pece, pece2) in enumerate(
            zip(time, euler_res, backward_euler_res, trapezoidal_res, runge_kutta_res,
                pece_res, pece2_res)):
        if i % print_step == 0:
            tab.append([t, euler, backward_euler, trapezoidal, runge_kutta, pece, pece2])

    with open("results/" + exercise + ".txt", "w") as f:
        f.write(tabulate.tabulate(tab, headers="firstrow", tablefmt="fancy_grid"))


def plot_graphs(time, euler_res, backward_euler_res, trapezoidal_res, runge_kutta_res,
                    pece_res, pece2_res, exercise, mathematical_pendulum_res = None):

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    if mathematical_pendulum_res:
        axs[0].plot(time, [x[0] for x in mathematical_pendulum_res], label="Analytic solution")
    axs[0].plot(time, [x[0] for x in euler_res], label="Euler")
    axs[0].plot(time, [x[0] for x in backward_euler_res], label="Backward Euler")
    axs[0].plot(time, [x[0] for x in trapezoidal_res], label="Trapezoidal")
    axs[0].plot(time, [x[0] for x in runge_kutta_res], label="Runge-Kutta")
    axs[0].plot(time, [x[0] for x in pece_res], label="PE(CE)")
    axs[0].plot(time, [x[0] for x in pece2_res], label="PE(CE)2")
    axs[0].legend()
    axs[0].set_title('x1')
    axs[0].set_xlabel('time')
    axs[0].set_ylabel('x1')

    if mathematical_pendulum_res:
        axs[1].plot(time, [x[1] for x in mathematical_pendulum_res], label="Analytic solution")
    axs[1].plot(time, [x[1] for x in euler_res], label="Euler")
    axs[1].plot(time, [x[1] for x in backward_euler_res], label="Backward Euler")
    axs[1].plot(time, [x[1] for x in trapezoidal_res], label="Trapezoidal")
    axs[1].plot(time, [x[1] for x in runge_kutta_res], label="Runge-Kutta")
    axs[1].plot(time, [x[1] for x in pece_res], label="PE(CE)")
    axs[1].plot(time, [x[1] for x in pece2_res], label="PE(CE)2")
    axs[1].legend()
    axs[1].set_title('x2')
    axs[1].set_xlabel('time')
    axs[1].set_ylabel('x2')

    plt.savefig("figures/" + exercise + ".png")




