# Дан список размера N.
# Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей).

import random  # Импортируем функцию рандом

mas = []  # Создаём список, куда будут внесены случайные числа
s = []  # Создаём вспомогательный списка
mas1 = []  # Создаём список для конечного результата
n = int(input("Введите количество чисел в списке: "))
for j in range(n):  # Цикл проходит n количество раз
    mas.append(random.randint(0, 20))  # Добавляется в список mas n количество чисел
print(f"В список занеслось {n} случайных чисел: ")
print(*mas)
mas = [500] + mas + [500]  # Расширяем список, чтобы не возникало ошибок при проверке крайних чисел
for i in range(1, len(mas) - 1):  # Проходим по списку от 2 элемента до предпоследнего (не считает крайние 500)
    if mas[i - 1] > mas[i] and mas[i + 1] > mas[i]:  # Проверка на локальный минимум
        s.append(mas[i])  # Заносим в список s локальные минимумы
        s = [500] + s + [500]  # Расширяем список, чтобы не возникало ошибок при проверке крайних чисел
        for g in range(1, len(s) - 1):  # Проходим по списку от 2 элемента до предпоследнего (не считает крайние 500)
            if s[g - 1] > s[g] and s[g + 1] > s[g]:  # Сравнение элементов массивов
                if mas[i] == s[g]:  # Если элементы равны, то..
                    mas1.append(mas[i] * mas[i])  # .. возводим в квадрат элемент и добавляем в конечный список
    else:  # Если число не локальный минимум то..
        mas1.append(mas[i])  # ..заносим его в список

print("Список с локальными минимумами возведенных в квадрат: ")
print(*mas1)  # Вывод конечного списка
