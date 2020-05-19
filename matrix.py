import copy


class Matrix:
    def __init__(self, lst):
        self.matrix = lst
        self.size = len(lst)

    def inverse(self):
        matrixCopy = copy.deepcopy(self.matrix)
        inverse = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            inverse.append(row)

        indices = list(range(self.size))
        for fd in range(self.size):
            fdCoef = 1.0 / matrixCopy[fd][fd]
            for j in range(self.size):
                matrixCopy[fd][j] *= fdCoef
                inverse[fd][j] = round(inverse[fd][j] * fdCoef, 3)
            for i in indices[0:fd] + indices[fd + 1:]:
                crCoef = matrixCopy[i][fd]
                for j in range(self.size):
                    matrixCopy[i][j] = matrixCopy[i][j] - crCoef * matrixCopy[fd][j]
                    inverse[i][j] = round(inverse[i][j] - crCoef * inverse[fd][j], 3)
        return Matrix(inverse)

    def product(self, matrix):
        result = [[0 for j in range(self.size)] for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                for n in range(self.size):
                    result[i][j] = round(result[i][j] + self.matrix[i][n] * matrix.matrix[n][j], 3)
        return Matrix(result)

    def __str__(self):
        string = ""
        for row in self.matrix:
            string += str(row) + "\n"
        return string


