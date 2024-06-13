#teraz zaczyam ćwiczyć IFy 

samochody =['bmw','Audi','volvo','toyota','fiat']

for samochod in samochody:
    if samochod =='bmw':
        print(samochod.upper())
    else:
        print(samochod.title())

print(samochody[1] == "audi")
print(samochody[1].lower() == "audi")

chciane_auto = "peugeot"

if chciane_auto != "volvo":
    print("daj mnie VOLVO")