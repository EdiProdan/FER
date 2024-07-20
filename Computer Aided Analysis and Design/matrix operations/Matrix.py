from typing import Self


class Matrix:
    def __init__(self, file_path=None, matrix=None):
        if matrix is None:
            self.matrix = self.read_matrix_from_file(file_path)
        elif file_path is None:
            self.matrix = matrix

        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.permutations = 0
        self.epsilon = 10 ** -9

    def __del__(self):
        self.matrix = [[]]

    def __str__(self):
        max_len = max([len(str(col)) for row in self.matrix for col in row])
        return "\n".join(["|" + " ".join([str(col).rjust(max_len) for col in row]) + "|" for row in self.matrix])
        # print a normal matrix with spaces
        # return "\n".join([" ".join([str(col) for col in row]) for row in self.matrix])
        # for row in self.matrix:
        #     return " ".join([str(col) for col in row])


    def __change_dimension(self, rows, cols, identity=False):

        for row in self.matrix:
            row += [0] * (cols - self.cols)

        for i in range(rows - self.rows):
            self.matrix.append([0] * cols)

        if identity:
            self.matrix = [[1 if i == j else 0 for j in range(cols)] for i in range(rows)]

        self.rows = rows
        self.cols = cols

    @staticmethod
    def read_matrix_from_file(file_path):

        if file_path is None:
            return [[]]
        try:
            with open(file_path, 'r') as f:
                matrix_rows = [line.split() for line in f.readlines()]

            rows = len(matrix_rows)
            cols = len(matrix_rows[0])

            matrix = [[float(matrix_rows[m][n]) for n in range(cols)] for m in range(rows)]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")

        return matrix

    def write_matrix_to_file(self, file_path):
        with open(file_path, 'w') as f:
            for row in self.matrix:
                f.write(" ".join([str(col) for col in row]) + "\n")

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def create_result_matrix(self, other):

        if self.rows == 0 or self.cols == 0:
            self.__change_dimension(other.rows, other.cols)
        elif other.rows == 0 or other.cols == 0:
            other.__change_dimension(self.rows, self.cols)

        result = Matrix()
        result.__change_dimension(self.rows, self.cols)
        return result

    def __add__(self, other):
        result = self.create_result_matrix(other)

        for row in range(self.rows):
            for col in range(self.cols):
                result[row][col] = self[row][col] + other[row][col]

        return result

    def __sub__(self, other):
        result = self.create_result_matrix(other)

        for row in range(self.rows):
            for col in range(self.cols):
                result[row][col] = self[row][col] - other[row][col]

        return result

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Number of columns in first matrix must be equal to number of rows in second matrix.")

            result = Matrix()
            result.__change_dimension(self.rows, other.cols)

            for row in range(self.rows):
                for col in range(other.cols):
                    for i in range(self.cols):
                        result[row][col] += self[row][i] * other[i][col]

            return result

        elif isinstance(other, (int, float)):
            result = Matrix()
            result.__change_dimension(self.rows, self.cols)

            for row in range(self.rows):
                for col in range(self.cols):
                    result[row][col] = self[row][col] * other

            return result

    def __rmul__(self, other):
        result = Matrix()
        result.__change_dimension(self.rows, self.cols)

        if isinstance(other, (int, float)):
            for row in range(self.rows):
                for col in range(self.cols):
                    result[row][col] = self[row][col] * other

        return result

    # division by scalar
    def __truediv__(self, other):
        result = Matrix()
        result.__change_dimension(self.rows, self.cols)

        if isinstance(other, (int, float)):
            for row in range(self.rows):
                for col in range(self.cols):
                    result[row][col] = self[row][col] / other

        return result

    def __invert__(self):
        result = Matrix()
        result.__change_dimension(self.cols, self.rows)

        for row in range(self.rows):
            for col in range(self.cols):
                result[col][row] = self[row][col]

        return result

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __eq__(self, other):
        for row in range(self.rows):
            for col in range(self.cols):
                if abs(self[row][col] - other[row][col]) > self.epsilon:
                    return False

        return True

    def backward_substitution(self, y) -> Self:
        x = Matrix()
        x.__change_dimension(self.rows, 1)
        try:
            if abs(self.matrix[self.cols - 1][self.cols - 1]) < self.epsilon:
                raise ZeroDivisionError("Division by zero in backward substitution.")

            x[self.cols - 1][0] = y[self.cols - 1][0] / self.matrix[self.cols - 1][self.cols - 1]
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero in backward substitution.")

        for i in reversed(range(0, self.rows - 1)):
            try:
                if abs(self.matrix[i][i]) < self.epsilon:
                    raise ZeroDivisionError("Division by zero in backward substitution.")

                x[i][0] = y[i][0] / self.matrix[i][i]
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero in backward substitution.")
            for j in range(i + 1, self.rows):
                x[i][0] -= (self.matrix[i][j] * x[j][0]) / self.matrix[i][i]
                if abs(x[i][0]) < self.epsilon:
                    x[i][0] = 0

        return x

    def forward_substitution(self, b) -> Self:
        y = Matrix()
        y.__change_dimension(self.rows, 1)
        y[0][0] = b[0][0]

        for i in range(1, self.rows):
            y[i][0] = b[i][0]
            for j in range(i):
                y[i][0] -= self.matrix[i][j] * y[j][0]

        return y

    def __get_l(self):
        L = Matrix()
        L.__change_dimension(self.rows, self.cols, identity=True)

        for i in range(self.rows):
            for j in range(i):
                L.matrix[i][j] = self.matrix[i][j]

        return L

    def __get_u(self):
        U = Matrix()
        U.__change_dimension(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(i, self.cols):
                U.matrix[i][j] = self.matrix[i][j]

        return U

    def __find_pivot(self, col):
        pivot = (col, col)
        for i in range(col + 1, self.rows):
            if abs(self.matrix[i][col]) > abs(self.matrix[pivot[0]][pivot[1]]):
                pivot = (i, col)

        if abs(self.matrix[pivot[0]][pivot[1]]) < self.epsilon:
            raise ValueError("Matrix is singular.")

        return pivot

    def lu_decomposition(self, lup=False):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square.")

        P = Matrix()
        P.__change_dimension(self.rows, self.cols, identity=True)

        for i in range(self.rows - 1):
            if lup:
                pivot = self.__find_pivot(i)
                if pivot[0] != i:
                    self.matrix[i], self.matrix[pivot[0]] = self.matrix[pivot[0]], self.matrix[i]
                    P.matrix[i], P.matrix[pivot[0]] = P.matrix[pivot[0]], P.matrix[i]
                    self.permutations += 1

            for j in range(i + 1, self.rows):
                try:
                    if abs(self.matrix[i][i]) < self.epsilon:
                        raise ZeroDivisionError("Division by zero in LU decomposition.")
                    self.matrix[j][i] /= self.matrix[i][i]
                except ZeroDivisionError:
                    raise ZeroDivisionError("Division by zero in LU decomposition.")

                for k in range(i + 1, self.rows):
                    self.matrix[j][k] -= self.matrix[j][i] * self.matrix[i][k]

        return P, self.__get_l(), self.__get_u()

    def __get_column(self, B, col):
        column = Matrix()
        column.__change_dimension(self.rows, 1)

        for i in range(self.rows):
            column[i][0] = B[i][col]

        return column

    def __write_column(self, result, column, col):
        for i in range(self.rows):
            result[i][col] = column[i][0]

    def inverse(self):

        P, _, _ = self.lu_decomposition(lup=True)

        result = Matrix()
        result.__change_dimension(self.rows, self.cols)

        b = Matrix()
        b.__change_dimension(self.rows, self.cols, identity=True)
        B = P * b
        for i in range(self.cols):
            B_i = self.__get_column(B, i)

            y_i = self.forward_substitution(B_i)

            x_i = self.backward_substitution(y_i)

            self.__write_column(result, x_i, i)

        return result

    def determinant(self, L, U):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square.")

        det = (-1) ** self.permutations
        for i in range(self.rows):
            det *= L[i][i] * U[i][i]

        return det
