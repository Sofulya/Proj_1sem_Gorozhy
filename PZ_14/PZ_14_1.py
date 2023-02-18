# В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя
# (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту).
# Посчитать количество полученных элементов.

import re

with open('Dostoevsky.txt', 'r',  encoding='UTF-8') as file:
    lst = re.findall(r'\d{4}.год\n|\d{4}.\d{4}.гг\.\n', ''.join([i for i in file.readlines()]))
    lst = [i[:-1] for i in lst]
    print(f"Список годов: {lst}\n"
          f"Количество полученных элементов: {len(lst)}")
