from functions import *
from lab.lab4.Constraints import Constraints
from utils import config
from lab.lab4.box import box
from lab.lab4.mixed_transformation import mixed_transformation

if __name__ == "__main__":

    epsilon = config["epsilon"]
    alpha = config["alpha"]

    # Exercise 1

    print("====================== Exercise 1 ======================")

    f_1_x_0 = config["exercise_1"]["f_1_x_0"]
    f_2_x_0 = config["exercise_1"]["f_2_x_0"]

    explicit_constraints = config["exercise_1"]["explicit_constraints"]

    implicit_constraints = [lambda x: x[1] - x[0], lambda x: 2 - x[0]]

    constraints = Constraints(explicit_constraints=explicit_constraints, implicit_constraints=implicit_constraints)

    box_optimizer = box(f_1_x_0, f_1, constraints, epsilon, alpha)
    print("Box optimizer for f_1: ", box_optimizer)

    box_optimizer = box(f_2_x_0, f_2, constraints, epsilon, alpha)
    print("Box optimizer for f_2: ", box_optimizer)

    print("\n====================== Exercise 2 ======================")

    implicit_constraints = [lambda x: x[1] - x[0], lambda x: 2 - x[0]]
    explicit_constraints = config["exercise_1"]["explicit_constraints"]
    t = config["exercise_2"]["t"]

    constraints = Constraints(explicit_constraints=explicit_constraints, implicit_constraints=implicit_constraints)

    mt_optimizer = mixed_transformation(f_1_x_0, f_1, constraints, epsilon)
    print("Mixed transformation optimizer for f_1: ", mt_optimizer)

    # feasible_f_1_x_0 = [1.1, 0.4]
    feasible_f_1_x_0 = [0.5, 1.5]

    mt_optimizer_feasible = mixed_transformation(feasible_f_1_x_0, f_1, constraints, epsilon)
    print("Mixed transformation optimizer for f_1 with new starting points: ", mt_optimizer_feasible)

    mt2_optimizer = mixed_transformation(f_2_x_0, f_2, constraints, epsilon)
    print("Mixed transformation optimizer for f_2: ", mt2_optimizer)

    print("\n====================== Exercise 3 ======================")

    f_4_x_0 = config["exercise_3"]["f_4_x_0"]
    implicit_constraints = [lambda x: 3 - x[0] - x[1], lambda x: 3 + 1.5*x[0] - x[1]]
    equality_constraints = [lambda x: x[1] - 1]

    constraints = Constraints(implicit_constraints=implicit_constraints, equality_constraints=equality_constraints)

    mt = mixed_transformation(f_4_x_0, f_4, constraints, epsilon)
    print("Mixed transformation optimizer for f_4: ", mt)

    err_f_4_x_0 = [5, 5]

    mt_err = mixed_transformation(err_f_4_x_0, f_4, constraints, epsilon)
    print("Mixed transformation optimizer for f_4 with new starting points: ", mt_err)

