# Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре.
# Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно поставив последнюю строку между второй и третьей.

file = open('text18-7.txt', encoding='UTF-8')
data = file.read()
count_letters = sum(map(str.islower, data))
print(f"Исходное стихотворение: \n{data}\n")
print(f"Количество букв в нижнем регистре: {count_letters}")
file.close()
file = open('new_text18-7.txt', 'w', encoding='UTF-8')

rows_from_one_to_second = data.splitlines()[:2]  # возвращаем строчки, первую и вторую
last_row = data.splitlines()[-1]
mid_rows = data.splitlines()[2:6]
print('\n'.join(rows_from_one_to_second) + '\n' + ''.join(last_row) + '\n' + '\n'.join(mid_rows), file=file)
file.close()
