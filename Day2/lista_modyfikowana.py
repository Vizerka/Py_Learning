#w tym pliku będę ćwiczyć operacje na listach, modyfikowanie i takie tam 
samohut = ['jetta', 's60', '940', 'civic', 'e46'] #pamiętaj o używaniu przecinków xD
print(samohut)
print("___________________________________________________________________")

#odwołam się teraz do 'jetta'
print(samohut[0])
print("___________________________________________________________________")

#zmienię 'jetta' na 'jetta mk2'
samohut[0] = "jetta mk2"
print(samohut)
print("___________________________________________________________________")

#dodam na końcu listy samohut 
print(samohut)
samohut.append('e36') #metoda append() dodaje na końcu listy element, bez modyfikacji pozostałych elementów
print(samohut)
print("___________________________________________________________________")

#metodą append() można zbudować pustą listę wypełniając ją danymi
samohut2 = []
samohut2.append('jetta mk2')
samohut2.append('s80')
samohut2.append('940')
samohut2.append('e46')
print(f"To jest lista samohut2 {samohut2}")
print("___________________________________________________________________")

#można też dodać element do listy w dowolnym miejscu za pomocą metody insert()
#w nawiasach metody wpisuje się nr indeksu w którym ma zostać wstawiony element
#reszta elementów zostanie przesunięta o jeden indeks w prawo
samohut2.insert(1, 'golf mk2')
print(f"Lista samohut2 po insert(1, golf mk2) {samohut2}")
print("___________________________________________________________________")

#skoro można dodać elementy to przydało by się też je usunąc
#można usunąć element z listy wg jego położenia, albo wartości
#usuwanie elementów z listy jest na podstawie położenia możliwe dzięki poleceniu del a następnie
#w nawiasach kwadratowych listy trzeba wpisać numer indeksu listy
#samohut2.del(1) nie tak xD
del samohut2[1] #tak xDD
print(f"Lista samohut2 po del samohut2[1] {samohut2}")
print("___________________________________________________________________")

#metoda pop(), nią można usunąć ostatni element listy ale zachowuje wartość usuniętego elementu w pamięci
usuniety_wpis = samohut2.pop()
print(f"Usunięty zapisany w pamięci wpis {usuniety_wpis}")
print(f"Lista samohut2 po pop() {samohut2}")
print("___________________________________________________________________")

#metodę pop() można też wykorzystać do usunięcia elementu wg numeru indeksu
#wysatrczy w nawiasach wpisać numer indeksu
moje_ulub_auto = samohut2.pop(0)
print(f"Moje ulubione auto to {moje_ulub_auto.title()}")
print(samohut2)
samohut2.append("jetta mk2")
print(f"Lista samohut2 po dodaniu jetta mk2 na końcu listy {samohut2}")
print("___________________________________________________________________")

#by usunąć element na liście wg zawartości należy użyć metody remove()
#w nawiasach metody należy wpisać zawartość elementu do usunięcia
samohut2.remove("940")
print(f"Lista samohut2 po użyciu metody remove('940') {samohut2}")