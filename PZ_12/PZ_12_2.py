# Составить генератор (yield), который преобразует все буквенные символы в строчные.

def ll(stroka):
    yield from [x.lower() for x in stroka]


print(''.join(ll(input("Введите строку: "))))
