import random
from typing import List


class Constraints:

    def __init__(self, explicit_constraints: List = None, implicit_constraints: List = None,
                 equality_constraints: List = None):
        self.explicit_constraints = explicit_constraints or []
        self.implicit_constraints = implicit_constraints or []
        self.equality_constraints = equality_constraints or []

    def check_explicit_constraints(self, x: List) -> List:
        for i in range(len(x)):
            R = random.uniform(0, 1)
            if x[i] < self.explicit_constraints[i][0]:
                x[i] = (self.explicit_constraints[i][0] + R *
                        (self.explicit_constraints[i][1] - self.explicit_constraints[i][0]))
            elif x[i] > self.explicit_constraints[i][1]:
                x[i] = (self.explicit_constraints[i][1] - R *
                        (self.explicit_constraints[i][1] - self.explicit_constraints[i][0]))

        return x

    def check_implicit_constraints(self, x: List, x_c: List, check_x_0: bool = False) -> List:
        for g_i in self.implicit_constraints:
            while g_i(x) < 0:
                for i in range(len(x)):
                    if check_x_0:
                        x[i] = 0.5 * (self.explicit_constraints[i][0] + self.explicit_constraints[i][1])
                    else:
                        x[i] = 0.5 * (x[i] + x_c[i])

        for g_i in self.implicit_constraints:
            if g_i(x) < 0:
                self.check_implicit_constraints(x, x_c, check_x_0)

        return x
