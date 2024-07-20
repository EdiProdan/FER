from golden_section_search import golden_section_search as golden_section
from coordinate_search import coordinate_search as coordinate_axis_search
from nelder_mead_method import nelder_mead_method as nelder_mead
from hooke_jeeves_method import hooke_jeeves_method as hooke_jeeves

from utils import config, round_nested_list

from functions import f_fibonacci, f, f1, f2, f3, f4, f6

from tabulate import tabulate
import random

if __name__ == '__main__':

    e = config['epsilon']
    k = config['k']
    h = config['h']
    dx = config['dx']
    alpha = config['alpha']
    beta = config['beta']
    gamma = config['gamma']
    sigma = config['sigma']

    print("\n====================== Exercise 1 ======================\n")

    x0 = config['x0_1']
    data_1 = []
    headers = ["Golden Section", "Evals", "Coordinate Search", "Evals", "Nelder-Mead", "Evals",
               "Hooke-Jeeves", "Evals"]

    gs = golden_section(x0=x0[0], h=h, e=e, k=k, f=f_fibonacci)
    gs_counter = f_fibonacci.counter
    f_fibonacci.counter = 0

    cas = coordinate_axis_search(f, x0, h, k, e)
    cas_counter = f.counter
    f.counter = 0
    simplex = nelder_mead(x0, h, alpha, beta, gamma, sigma, e, f)
    simplex_counter = f.counter
    f.counter = 0
    xb = hooke_jeeves(x0, dx, e, f)
    xb_counter = f.counter
    f.counter = 0
    data_1.append([gs[1], gs_counter, cas[0][0], cas_counter, simplex[0][0], simplex_counter, xb[0][0], xb_counter])
    rounded_data_1 = round_nested_list(data_1, 5)
    print(tabulate(rounded_data_1, headers, tablefmt="grid"))
    with open('results/exercise1.txt', 'w') as file:
        file.write(tabulate(data_1, headers, tablefmt="grid"))

    print("\n====================== Exercise 2 ======================\n")

    headers = ["f", "Nelder-Mead", "NM Eval", "Hooke-Jeeves", "HJ Eval", "Coordinate", "Coord Eval"]
    data = []

    starting_point_1 = config['x0_2_1']
    nelder_mead_min = nelder_mead(starting_point_1, h, alpha, beta, gamma, sigma, e, f1)
    simplex_counter = f1.counter
    f1.counter = 0
    hooke_jeeves_min = hooke_jeeves(starting_point_1, dx, e, f1)
    xb_counter = f1.counter
    f1.counter = 0
    cas = coordinate_axis_search(f1, starting_point_1, h, k, e)
    cas_counter = f1.counter
    f1.counter = 0
    data.append(
        ["f1", nelder_mead_min[0], simplex_counter, hooke_jeeves_min[0], xb_counter, cas[0], cas_counter])

    starting_point_2 = config['x0_2_2']
    nelder_mead_min = nelder_mead(starting_point_2, h, alpha, beta, gamma, sigma, e, f2)
    simplex_counter = f2.counter
    f2.counter = 0
    hooke_jeeves_min = hooke_jeeves(starting_point_2, dx, e, f2)
    xb_counter = f2.counter
    f2.counter = 0
    cas = coordinate_axis_search(f2, starting_point_2, h, k, e)
    cas_counter = f2.counter
    f2.counter = 0
    data.append(
        ["f2", nelder_mead_min[0], simplex_counter, hooke_jeeves_min[0], xb_counter, cas[0], cas_counter])

    starting_point_3 = config['x0_2_3']
    dx_3 = config['dx_2_3']
    nelder_mead_min = nelder_mead(starting_point_3, h, alpha, beta, gamma, sigma, e, f3)
    simplex_counter = f3.counter
    f3.counter = 0
    hooke_jeeves_min = hooke_jeeves(starting_point_3, dx_3, e, f3)
    xb_counter = f3.counter
    f3.counter = 0
    cas = coordinate_axis_search(f3, starting_point_3, h, k, e)
    cas_counter = f3.counter
    f3.counter = 0
    data.append(
        ["f3", nelder_mead_min[0], simplex_counter, hooke_jeeves_min[0], xb_counter, cas[0], cas_counter])

    starting_point_4 = config['x0_2_4']
    nelder_mead_min = nelder_mead(starting_point_4, h, alpha, beta, gamma, sigma, e, f4, trace=False)
    simplex_counter = f4.counter
    f4.counter = 0
    hooke_jeeves_min = hooke_jeeves(starting_point_4, dx, e, f4, trace=False)
    xb_counter = f4.counter
    f4.counter = 0
    cas = coordinate_axis_search(f4, starting_point_4, h, k, e)
    cas_counter = f4.counter
    f4.counter = 0
    data.append(
        ["f4", nelder_mead_min[0], simplex_counter, hooke_jeeves_min[0], xb_counter, cas[0], cas_counter])

    for row in data:
        row[1] = round_nested_list(row[1])
        row[3] = round_nested_list(row[3])
        row[5] = round_nested_list(row[5])

    print(tabulate(data, headers, tablefmt="grid"))
    with open('results/exercise2.txt', 'w') as file:
        file.write(tabulate(data, headers, tablefmt="grid"))

    print("\n====================== Exercise 3 ======================\n")
    starting_point = config['x0_3_1']
    data_3 = []
    headers = ["f", "Nelder-Mead x_min", "Nelder-Mead", "NM Eval", "Hooke-Jeeves x_min", "Hooke-Jeeves", "HJ Eval"]

    nelder_mead_min = nelder_mead(starting_point, h, alpha, beta, gamma, sigma, e, f4, trace=False)
    simplex_counter = f4.counter
    f4.counter = 0
    hooke_jeeves_min = hooke_jeeves(starting_point, dx, e, f4, trace=False)
    xb_counter = f4.counter
    f4.counter = 0
    data_3.append(
        ["f4", nelder_mead_min[0], nelder_mead_min[1], simplex_counter, hooke_jeeves_min[0], hooke_jeeves_min[1],
         xb_counter])
    for row in data_3:
        row[1] = round_nested_list(row[1])
        row[4] = round_nested_list(row[4])

    print(tabulate(data_3, headers, tablefmt="grid"))
    with open('results/exercise3.txt', 'w') as file:
        file.write(tabulate(data_3, headers, tablefmt="grid"))

    print("\n====================== Exercise 4 ======================\n")

    starting_points = [[0.5, 0.5], [20, 20]]
    hs = [1, 5, 10, 15, 20]
    data_4 = []
    header = ["h", "Starting Point", "Nelder-Mead x_min", "Nelder-Mead Evaluations"]

    for starting_point in starting_points:
        for h in hs:
            nelder_mead_min = nelder_mead(starting_point, h, alpha, beta, gamma, sigma, e, f1, trace=False)
            simplex_counter = f1.counter
            f1.counter = 0
            data_4.append([h, starting_point, nelder_mead_min[0], simplex_counter])

    for row in data_4:
        row[2] = round_nested_list(row[2])

    print(tabulate(data_4, header, tablefmt="grid"))
    with open('results/exercise4.txt', 'w') as file:
        file.write(tabulate(data_4, header, tablefmt="grid"))

    print("\n====================== Exercise 5 ======================\n")

    dx = config['dx']
    counter = 0
    while True:
        counter += 1
        starting_point_6 = [random.uniform(-50, 50), random.uniform(-50, 50)]
        simplex = nelder_mead(starting_point_6, h, alpha, beta, gamma, sigma, e, f6, trace=False)
        if simplex[1] < 10 ** -4:
            break

    output_str = f"""Potrebno je {counter} pokretanja Nelder-Mead metode da bi se pronašla točka koja zadovoljava uvjet.
Točka je {starting_point_6}, a minimum je {simplex[0]}, s vrijednošću funkcije {simplex[1]}"""
    print(output_str)
    with open('results/exercise5.txt', 'w') as file:
        file.write(output_str)
