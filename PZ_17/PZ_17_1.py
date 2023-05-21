# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.

from random import randint


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[]]

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.grid]) + '\n'

    @staticmethod
    def out(lst):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in lst]) + '\n'

    def __add__(self, other):
        return self.out([[self.grid[i][j] + other.grid[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        return self.out([[self.grid[i][j] - other.grid[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other):
        return self.out([[sum([self.grid[i][k] * other.grid[k][j] for k in range(self.cols)]) for j in range(self.cols)]
                         for i in range(self.rows)])


# Создание матриц
a = Matrix(3, 3)
a.grid = [[randint(1, 10) for _ in range(a.cols)] for _ in range(a.rows)]
print('Матрица a:')
print(a)

b = Matrix(3, 3)
b.grid = [[randint(1, 10) for _ in range(b.cols)] for _ in range(b.rows)]
print('Матрица b:')
print(b)

print('Сложение матриц:')
print(a + b)

print('Вычитание матриц:')
print(a - b)

print('Умножение матриц:')
print(a * b)
