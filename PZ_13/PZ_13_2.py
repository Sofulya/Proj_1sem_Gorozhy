#  В матрице элементы последнего столбца заменить на -1

from random import randint

#  Заносим в переменные параметры матрицы
a, b, c, d = [int(input(i)) for i in ("Количество строк: ", "Количество столбцов: ", "От = ", "До = ")]
#  Заполнение матрицы случайными числами
matrix = [[randint(c, d) for _ in range(b)] for j in range(a)]
print("Исходная матрица: ", '\n', [i for i in matrix])
#  Замена последних элементов в строке на -1
for i in range(a):
    matrix[i][b - 1] = -1
print("Полученная матрица: ", '\n', [i for i in matrix])
