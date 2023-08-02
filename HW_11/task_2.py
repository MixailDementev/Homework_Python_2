# Создайте класс Матрица.
# Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(
            other.matrix[0]
        ):
            return f"Error: матрицы разных размеров"
        else:
            return Matrix(
                [
                    [
                        self.matrix[i][j] + other.matrix[i][j]
                        for j in range(len(self.matrix[0]))
                    ]
                    for i in range(len(self.matrix))
                ]
            )

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            return f"Error: невозможно перемножить матрицы"
        else:
            new_matrix = [
                [
                    sum(i * j for i, j in zip(i_row, j_col))
                    for j_col in zip(*other.matrix)
                ]
                for i_row in self.matrix
            ]
            return Matrix(new_matrix)

    def __eq__(self, other):
        return self.get_matrix() == other.get_matrix()

    def __str__(self):
        matrix = ""
        for i in range(len(self.matrix)):
            matrix += str(self.matrix[i]) + "\n"
        return matrix


if __name__ == "__main__":
    matrix_1 = Matrix([[1, 2, 4], [5, 6, 8], [2, 5, -2], [10, 5, 0]])
    matrix_2 = Matrix([[1, 3, -1], [5, 6, 8], [5, 6, 8], [-2, 2, 0]])
    matrix_3 = Matrix([[5, 2, 4, 9], [5, 6, 8, 0], [5, 0, -7, 1]])
    matrix_4 = Matrix([[-1, 2, 7, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]])

    print("Cложение матриц:")
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)

    print("Умножение матриц:")
    matrix_mul = matrix_1 * matrix_3
    print(matrix_mul)
    print(matrix_1 * matrix_4)

    print("Cравнение матриц:")
    print(matrix_1 == matrix_1)
    print(matrix_1 == matrix_2)
