def f_1(x: list) -> float:
    """
    x_min = [1, 1], f(x_min) = 0
    """
    f_1.eval_count += 1
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


# write f1 as system of nonlinear equations g(x1) and g(x2)
def g_1(x: list) -> float:
    """
    g_1(x1, x2) = 10 * (x2 - x1^2)
    """
    return 10 * (x[1] - x[0] ** 2)


def g_2(x: list) -> float:
    """
    g_2(x1, x2) = 1 - x1
    """
    return 1 - x[0]


G = [g_1, g_2]


def dg_1_x_1(x: list) -> float:
    """
    dg_1/dx_1
    """
    return -20 * x[0]


def dg_1_x_2(x: list) -> float:
    """
    dg_1/dx_2
    """
    return 10


def dg_2_x_1(x: list) -> float:
    """
    dg_2/dx_1
    """
    return -1


def dg_2_x_2(x: list) -> float:
    """
    dg_2/dx_2
    """
    return 0


g_second_derivatives_list = [[dg_1_x_1, dg_1_x_2], [dg_2_x_1, dg_2_x_2]]


def df_1_x_1(x: list) -> list:
    """
    df_1/dx_1
    """
    df_1_x_2.eval_count += 1
    return -400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])


def df_1_x_2(x: list) -> list:
    """
    df_1/dx_2
    """
    df_1_x_2.eval_count += 1
    return 200 * (x[1] - x[0] ** 2)


# second derivatives
def d2f_1_x_1_x_1(x: list) -> float:
    """
    # df_1_x_0 -400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])
    d2f_1/dx_0^2
    """
    return -400 * (x[1] - x[0] ** 2) + 800 * x[0] ** 2 + 2


def d2f_1_x_1_x_2(x: list) -> float:
    """
    d2f_1/dx_1dx_2
    """
    return -400 * x[0]


def d2f_1_x_2_x_1(x: list) -> float:
    """
    d2f_1/dx_2dx_1
    """
    return -400 * x[0]


def d2f_1_x_2_x_2(x: list) -> float:
    """
    d2f_1/dx_2^2
    """
    return 200


f1_derivatives_list = [df_1_x_1, df_1_x_2]
f1_second_derivatives_list = [[d2f_1_x_1_x_1, d2f_1_x_1_x_2], [d2f_1_x_2_x_1, d2f_1_x_2_x_2]]


def f_2(x: list) -> float:
    """
    x_min = [4, 2], f(x_min) = 0
    """
    f_2.eval_count += 1
    return (x[0] - 4) ** 2 + 4 * (x[1] - 2) ** 2


def df_2_x_1(x: list) -> float:
    """
    df_2/dx_1
    """
    df_2_x_1.eval_count += 1
    return 2 * (x[0] - 4)


def df_2_x_2(x: list) -> float:
    """
    df_2/dx_2
    """
    df_2_x_2.eval_count += 1
    return 8 * (x[1] - 2)


def d2f_2_x_1_x_1(x: list) -> float:
    """
    d2f_2/dx_1^2
    """
    return 2


def d2f_2_x_1_x_2(x: list) -> float:
    """
    d2f_2/dx_1dx_2
    """
    return 0


def d2f_2_x_2_x_1(x: list) -> float:
    """
    d2f_2/dx_2dx_1
    """
    return 0


def d2f_2_x_2_x_2(x: list) -> float:
    """
    d2f_2/dx_2^2
    """
    return 8


f2_derivatives_list = [df_2_x_1, df_2_x_2]
f2_second_derivatives_list = [[d2f_2_x_1_x_1, d2f_2_x_1_x_2], [d2f_2_x_2_x_1, d2f_2_x_2_x_2]]


def f_3(x: list) -> float:
    """
    x_min = [2, -3], f(x_min) = 0
    """
    f_3.eval_count += 1
    return (x[0] - 2) ** 2 + (x[1] + 3) ** 2


def df_3_x_1(x: list) -> float:
    """
    df_3/dx_1
    """
    df_3_x_1.eval_count += 1
    return 2 * (x[0] - 2)


def df_3_x_2(x: list) -> float:
    """
    df_3/dx_2
    """
    df_3_x_2.eval_count += 1
    return 2 * (x[1] + 3)


f3_derivatives_list = [df_3_x_1, df_3_x_2]


def f_4(x: list) -> float:
    f_4.eval_count += 1
    return 1 / 4 * x[0] ** 4 - x[0] ** 2 + 2 * x[0] + (x[1] - 1) ** 2


def df_4_x_1(x: list) -> float:
    df_4_x_1.eval_count += 1
    return x[0] ** 3 - 2 * x[0] + 2


def df_4_x_2(x: list) -> float:
    df_4_x_2.eval_count += 1
    return 2 * (x[1] - 1)


def d2f_4_x_1_x_1(x: list) -> float:
    return 3 * x[0] ** 2 - 2


def d2f_4_x_1_x_2(x: list) -> float:
    return 0


def d2f_4_x_2_x_1(x: list) -> float:
    return 0


def d2f_4_x_2_x_2(x: list) -> float:
    return 2


f4_derivatives_list = [df_4_x_1, df_4_x_2]
f4_second_derivatives_list = [[d2f_4_x_1_x_1, d2f_4_x_1_x_2], [d2f_4_x_2_x_1, d2f_4_x_2_x_2]]


def g_5(x: list) -> float:
    return (x[0]**2 + x[1]**2 - 1)**2 + (x[1] - x[0]**2)**2


def g_1_exercise_5(x: list) -> float:
    return x[0]**2 + x[1]**2 - 1


def g_2_exercise_5(x: list) -> float:
    return x[1] - x[0]**2


def dg_1_exercise_5_x_1(x: list) -> float:
    return 2 * x[0]


def dg_1_exercise_5_x_2(x: list) -> float:
    return 2 * x[1]


f_1.eval_count = 0
f_2.eval_count = 0
f_3.eval_count = 0
f_4.eval_count = 0
df_1_x_1.eval_count = 0
df_1_x_2.eval_count = 0
df_2_x_1.eval_count = 0
df_2_x_2.eval_count = 0
df_3_x_1.eval_count = 0
df_3_x_2.eval_count = 0
df_4_x_1.eval_count = 0
df_4_x_2.eval_count = 0
def dg_2_exercise_5_x_1(x: list) -> float:
    return -2 * x[0]


def dg_2_exercise_5_x_2(x: list) -> float:
    return 1


G_exercise_5 = [g_1_exercise_5, g_2_exercise_5]
g_second_derivatives_list_exercise_5 = [[dg_1_exercise_5_x_1, dg_1_exercise_5_x_2],
                                        [dg_2_exercise_5_x_1, dg_2_exercise_5_x_2]]

