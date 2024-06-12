for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)
liczby = list(range(1,6))
print(liczby)

parzyste_liczby = list(range(2,11,2))
print(parzyste_liczby)

kwadraty = list(range(1,11))
kwadraty2 =[]
for kwadrat in kwadraty:
    wartosc=kwadrat**2
    print(wartosc)
    kwadraty2.append(wartosc)
print(kwadraty2)
