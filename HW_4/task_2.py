# Напишите функцию для транспонирования матрицы


def transport_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transport_matrix(matrix)
print(transposed)