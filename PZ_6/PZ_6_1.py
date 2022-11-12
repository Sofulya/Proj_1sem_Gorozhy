# Дан целочисленный список размера 10.
# Вывести все содержащиеся в данном списке нечетные числа в порядке возрастания их индексов,
# а также их количество K.
import random  # Импортируем функцию рандом

mas = []  # Создаём список, в котором будут начальные данные
s = []  # Создаём список, в котором будут конечные результаты
k = 0  # Счётчик суммы нечётных чисел
for i in range(10):  # Цикл проходит n количество раз
    mas.append(random.randint(1, 50))  # Добавляется в список mas n количество чисел
print("В список занеслось 10 случайных чисел: ")
print(*mas)
for i, x in enumerate(mas):  # Проходит по массиву mas, enumerate возвращает индекс и число в списке
    if x % 2 != 0:  # Проверяем на нечётность
        print("Элемент №", i, "это: ", x)
        k += 1  # Счётчик суммы нечётных чисел
        s.append(x)  # Заносим нечётные числа в новый массив
print("Числа в порядке возрастания их индексов: ")
print(*s)  # Выводим конечный список в порядке возрастания их индексов
print(f"Количество нечетных чисел: {k}")  # Вывод количества нечётных чисел
