from matrix import Matrix


class Model:
    def __init__(self):
        beta = float(input("Enter infection rate: "))
        dr = float(input("Enter death rate: "))
        te = float(input("Enter average time person is exposed: "))
        it = float(input("Enter average time person is infectious: "))
        self.F = Matrix([[0, beta], [0, 0]])
        self.V = Matrix([[min(1/te + dr, 1), 0], [-1/te, min(1/it + dr, 1)]])

    def calculate(self):
        return self.F.product(self.V.inverse()).matrix[0][0]


if __name__ == '__main__':
    model = Model()
    print(model.calculate())
