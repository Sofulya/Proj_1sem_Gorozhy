# Составить генератор (yield), который преобразует все буквенные символы в строчные.

def ll(stroka):
    yield from [i.lower() for i in stroka]


print(''.join(ll(input("Введите строку: "))))
