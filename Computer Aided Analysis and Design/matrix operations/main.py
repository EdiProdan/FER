from Matrix import Matrix

if __name__ == "__main__":
    # Example 1
    print("================= Example 1 =================")

    A_1 = Matrix("matrices/A_2.txt")
    print("A_1:")
    print(A_1 == A_1 * 2.3 / 2.3)

    # Example 2_1.txt
    print("================= Example 2 =================")
    A_2 = Matrix("matrices/A_2.txt")
    b_2 = Matrix("matrices/b_2.txt")
    print("Solution of Ax = b using LU decomposition:")
    try:
        P, L, U = A_2.lu_decomposition()
        y = L.forward_substitution(P * b_2)
        x = U.backward_substitution(y)
        print(x)
        x.write_matrix_to_file("results/2_1.txt")
    except ZeroDivisionError as e:
        with open("results/2_1.txt", "w") as f:
            f.write(str(e))
        print(e)

    # Example 2.2
    A_2 = Matrix("matrices/A_2.txt")
    b_2 = Matrix("matrices/b_2.txt")
    P, L, U = A_2.lu_decomposition(lup=True)
    y = L.forward_substitution(P * b_2)
    x = U.backward_substitution(y)
    print("\nSolution of Ax = b using LUP decomposition:")
    print(x)
    x.write_matrix_to_file("results/2_2.txt")



    # Example 3.1
    print("\n================= Example 3 =================")
    A_3 = Matrix("matrices/A_3.txt")
    try:
        P, L, U = A_3.lu_decomposition()
        y = L.forward_substitution(P * b_2)
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LU decomposition:")
        print(x)
        x.write_matrix_to_file("results/3_1.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/3_1.txt", "w") as f:
            f.write(str(e))

    A_3 = Matrix("matrices/A_3.txt")
    try:
        P, L, U = A_3.lu_decomposition(lup=True)
        y = L.forward_substitution(P * b_2)
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LUP decomposition:")
        print(x)
        x.write_matrix_to_file("results/3_2.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/3_2.txt", "w") as f:
            f.write(str(e))


    ## Example 4
    print("\n================= Example 4 =================")
    A_4 = Matrix("matrices/A_4.txt")
    b_4 = Matrix("matrices/b_4.txt")
    try:
        P, L, U = A_4.lu_decomposition()
        y = L.forward_substitution(P * b_4)
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LU decomposition:")
        print(x)
        x.write_matrix_to_file("results/4_1.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/4_1.txt", "w") as f:
            f.write(str(e))

    A_4 = Matrix("matrices/A_4.txt")
    try:
        P, L, U = A_4.lu_decomposition(lup=True)
        y = L.forward_substitution(P * b_4)
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LUP decomposition:")
        print(x)
        x.write_matrix_to_file("results/4_2.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/4_2.txt", "w") as f:
            f.write(str(e))


    ## Example 5
    print("\n================= Example 5 =================")
    A_5 = Matrix("matrices/A_5.txt")
    b_5 = Matrix("matrices/b_5.txt")
    try:
    # P, L, U = A_5.lu_decomposition()
        P, L, U = A_5.lu_decomposition(lup=True)
        y = L.forward_substitution(P * b_5)
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LUP decomposition:")
        print(x)
        x.write_matrix_to_file("results/5_1.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/5_1.txt", "w") as f:
            f.write(str(e))

    A_5 = Matrix("matrices/A_5.txt")
    try:
        P, L, U = A_5.lu_decomposition()
        y = L.forward_substitution(P * b_5)
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LU decomposition:")
        print(x)
        x.write_matrix_to_file("results/5_2.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/5_2.txt", "w") as f:
            f.write(str(e))

    ## Example 6
    print("\n================= Example 6 =================")
    A_6 = Matrix("matrices/A_6.txt")
    b_6 = Matrix("matrices/b_6.txt")
    try:
        # change epsilon to 1e-10
        A_6.epsilon = 10 ** -6
        P, L, U = A_6.lu_decomposition()
        print("P:")
        print(P)
        print("L:")
        print(L)
        print("U:")
        print(U)
        y = L.forward_substitution(P * b_6)
        U.epsilon = 10 ** -6
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LU decomposition:")
        print(x)
        x.write_matrix_to_file("results/6_1.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/6_1.txt", "w") as f:
            f.write(str(e))

    A_6 = Matrix("matrices/A_6.txt")
    try:
        A_6.epsilon = 10 ** -6
        P, L, U = A_6.lu_decomposition(lup=True)
        print("P:")
        print(P)
        print("L:")
        print(L)
        print("U:")
        print(U)
        y = L.forward_substitution(P * b_6)
        print("y:")
        print(y)
        U.epsilon = 10 ** -6
        x = U.backward_substitution(y)
        print("\nSolution of Ax = b using LUP decomposition:")
        print(x)
        x.write_matrix_to_file("results/6_2.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/6_2.txt", "w") as f:
            f.write(str(e))



    ## Example 7
    print("\n================= Example 7 =================")
    A_7 = Matrix("matrices/A_7.txt")
    try:
        P, L, U = A_7.lu_decomposition(lup=True)
        A_7_inv = A_7.inverse(P)
        print("A_7 inverse:")
        print(A_7_inv)
        A_7_inv.write_matrix_to_file("results/7.txt")
    except ZeroDivisionError as e:
        print(e)
        with open("results/7.txt", "w") as f:
            f.write(str(e))

    ## Example 8
    print("\n================= Example 8 =================")
    A_8 = Matrix("matrices/A_8.txt")
    P, L, U = A_8.lu_decomposition(lup=True)
    A_8_inv = A_8.inverse(P)
    print("A_8 inverse:")
    print(A_8_inv)
    A_8_inv.write_matrix_to_file("results/8.txt")

    ## Example 9
    print("\n================= Example 9 =================")
    A_8_det = A_8.determinant(L, U)
    print(f"A_8 determinant = {A_8_det}")
    with open("results/9.txt", "w") as f:
        f.write(str(A_8_det))

    ## Example 10
    print("\n================= Example 10 =================")

    A_2 = Matrix("matrices/A_2.txt")
    P, L, U = A_2.lu_decomposition(lup=True)
    A_2_det = A_2.determinant(L, U)
    print(f"A_2 determinant = {A_2_det}")
    with open("results/10.txt", "w") as f:
        f.write(str(A_2_det))


