#krotka to niemodyfikowalna lista
rozmiary = (200,50)
print(rozmiary[0])
print(rozmiary[1])
#rozmiary[1]=30 nie można zmienić 
#definiowanie jednoelementowej krotki
jeden_ele_krot = (4,)
#krotka jest definiowana poprzez przecinek, w przypadku jednego elementu musi po nim być przecinek

rozmiary = (400,100)
print(f"to są nowe rozmiary krotki {rozmiary}")

#menu
menu = ("siusiak", "penis", "gigahuj","kutasik","szabrownik")

print(f"Nasza restauracja ma do zaoferowania taką gamę potraw:")
for item in menu:
    print(item)
#menu[1]="skutangens" no nie moszna
#a teraz zmiana
    
menu = ("hehe beniz", "penis", "gigahuj","kutasik","szabrownik")

print(f"Nasza restauracja ma do zaoferowania taką gamę potraw:")
for item in menu:
    print(item)