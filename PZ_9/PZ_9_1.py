#  Дана строка "груши 45 991 63 100 12 морковь 13 47 26 0 16",
#  отражаются продажи продукции по дням в кг. Преобразовать информацию из строки в словари,
#  с использованием функции найти минимальные продажи по каждому виду продукции, результаты вывести на экран.

a = "груши 45 991 63 100 12 морковь 13 47 26 0 16".split(" ")  # Делаем из строки список с помощью split
print("Дана строка: ", *a)
sg = []  # Создаем список, в который будут помещены продажи груш
sm = []  # Создаем список, в который будут помещены продажи моркови
for i in a[1:6]:  # Проходим по всем значениям груш
    sg.append(int(i))  # Добавляем в список эти элементы
for j in a[7:]:  # Проходим по всем элементам моркови
    sm.append(int(j))  # Добавляем в список эти элементы

slg = {a[0]: sg}  # Создаём словарь, где присваиваем груши - ключ, а числам значения
slm = {a[6]: sm}  # Создаём словарь, где присваиваем морковь - ключ, а числам значения


def minimal_product():  # Создаём функцию, находим минимальные продажи по каждому виду продукции
    # (минимальный элемент в словарях)
    print("Минимальная продажа груш составляет: ", min(slg["груши"]), "кг")
    print("Минимальная продажа моркови составляет: ", min(slm["морковь"]), "кг")


minimal_product()  # Вызов функции
