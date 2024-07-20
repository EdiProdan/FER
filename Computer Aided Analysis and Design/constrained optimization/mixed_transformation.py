from typing import Callable

import math

from lab.lab2.hooke_jeeves_method import hooke_jeeves_method
from lab.lab4.Constraints import Constraints


def transformed_function(x, constraints: Constraints, t, f: Callable):
    if any(func(x) <= 0 for func in constraints.implicit_constraints):
        return math.inf
    return f(x) - 1.0 / t * sum(math.log(func(x)) for func in constraints.implicit_constraints) + t * sum(
        math.pow(constraint(x), 2) for constraint in constraints.equality_constraints)


def internal_feasible_point(x, t, violated_constraints):
    penalty = sum(-t * f(x) for f in violated_constraints)
    if penalty < -0.0001:
        return math.inf
    return penalty


def mixed_transformation(x0: list, f: Callable, constraints: Constraints, e: float):
    t = 1
    dx = [0.5, 0.5]
    loop_counter = 0
    min_obj_fun = transformed_function(x0, constraints, t, f)
    while True:
        violated_constraints = [i_c for i_c in constraints.implicit_constraints if i_c(x0) < 0]
        if violated_constraints:
            x0 = hooke_jeeves_method(x0, dx, e, lambda x: internal_feasible_point(x, t, violated_constraints))[0]

        new_x0 = hooke_jeeves_method(x0, dx, e, lambda x: transformed_function(x, constraints, t, f))[0]

        if all(abs(a - b) < e for a, b in zip(x0, new_x0)):
            return new_x0

        x0 = new_x0

        if transformed_function(x0, constraints, t, f) < min_obj_fun:
            min_obj_fun = transformed_function(x0, constraints, t, f)
            loop_counter = 0

        loop_counter += 1
        if loop_counter >= 100:
            print("No improvement in 100 iterations. Stopping.")
            return x0

        t *= 10

