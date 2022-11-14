# Дан список размера N.
# Найти минимальный из его локальных максимумов.
# Локальный максимум - число, которое будет больше обоих из своих соседей.

import random  # Импортируем функцию рандом.

mas = []  # Создаём список, в котором будут начальные данные
s = []  # Создаём список, в котором будут конечные результаты
n = input("Введите количество чисел в списке: ")
while True:  # Программа работает, даже при ошибке
    try:  # Пользователь ввёл число
        n = int(n)
        break  # Досрочно прерывает цикл
    except ValueError:  # Проверка исключений(пользователь ввел не число)
        print("Введите число, пожалуйста!")
        n = input("Введите количество чисел в списке: ")
for j in range(n):  # Цикл проходит n количество раз
    mas.append(random.randint(0, 50))  # Добавляем в список mas n количество чисел
print(f"В список занеслось {n} случайных чисел: ")
print(*mas)
mas = [-1] + mas + [-1]  # Расширяем список, чтобы не возникало ошибок при проверке крайних чисел
for i in range(1, len(mas) - 1):  # Проходим по списку от 2 элемента до предпоследнего (не считает крайние -1)
    if mas[i] > mas[i - 1]:  # Проверяем на локальный минимум
        if mas[i] > mas[i + 1]:  # Проверяем на локальный минимум
            s.append(mas[i])  # Заносим в список s локальные минимумы

print("В списке найдены следующие локальные максимумы: ")
print(*s)  # Вывод самого списка локальных максимумов
print("Наименьший из локальных максимумов = ", min(s))  # В списке s с помощью функции min находим минимальный элемент.
