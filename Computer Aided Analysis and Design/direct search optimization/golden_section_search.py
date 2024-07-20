from typing import Callable, Tuple


def unimodal_interval(x: float, h: float, f: Callable) -> Tuple:
    left = x - h
    right = x + h
    middle = x
    step = 1

    fm = f(x)

    fl = f(left)
    # print(fl)
    fr = f(right)
    count = 0
    if fm < fr and fm < fl:
        return left, right

    elif fm > fr:
        while True:
            left = middle
            middle = right
            fm = fr
            step *= 2
            right = x + h * step
            fr = f(right)
            count += 1
            if fm < fr:
                break
    else:
        while True:
            right = middle
            middle = left
            fm = fl
            step *= 2
            left = x - h * step
            count += 1
            fl = f(left)

            if fm < fl:
                break
    return left, right


def golden_section_search(a: int = None, b: int = None, x0: float = None, h: int = None, e: float = None,
                          k: float = None, f: Callable = None, trace: bool = False) -> Tuple:
    """
    :param a: Left border of unimodal interval.
    :param b: Right border of unimodal interval.
    :param x0: Starting x.
    :param h: Step.
    :param e: Precision.
    :param k: Golden ratio constant.
    :param f: Unimodal function.
    :param trace: If True, print each iteration.

    :return: Interval of minimum.

    """
    if a is None and b is None:
        a, b = unimodal_interval(x0, h, f)

    c = b - k * (b - a)
    d = a + k * (b - a)

    fc = f(c)
    fd = f(d)

    if trace:
        print("a = {:.5f}    b = {:.5f}    c = {:.5f}    d = {:.5f}".format(a, b, c, d))
        print("f(a) = {:.5f} f(b) = {:.5f} f(c) = {:.5f} f(d) = {:.5f}".format(f(a), f(b), f(c), f(d)))
        print("============================================================")

    while (b - a) > e:
        if fc < fd:
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = f(c)
        else:
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = f(d)

        if trace:
            print("a = {:.5f}    b = {:.5f}    c = {:.5f}    d = {:.5f}".format(a, b, c, d))
            print("f(a) = {:.5f} f(b) = {:.5f} f(c) = {:.5f} f(d) = {:.5f}".format(f(a), f(b), f(c), f(d)))
            print("============================================================")

    return a, b
