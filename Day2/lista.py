#w tym pliku zaczynam używać list
#Listy tworzy się po przez użycie nawiasów kwadratowych []

lista = ['Pierwszy wpis', 'Drugi wpis','Trzeci wpis', 'Czwarty wpis']
print(lista)

#w celu odwołania się do poszczególnych elementów listy trzeba użyć indeksu w nawiasie kwadratowym
print(lista[0]) #pamiętaj że numeracja zaczyna się od zera, więc pierwszy wpis ma indeks "0"

#w przypadku chęci odwołania się do ostatniego elementu listy można użyć indeksu -1
print(lista[-1])

#używanie poszczególnych elementów listy 
print(f"Moim pierwszym wpisem na liście jest '{lista[0].upper()}'")

#kilka kolejnych ćwiczeń z listami
imionka = ['wiktoria', 'astryda', 'klaudia', 'felicja']
print(f"Moja znajoma ma na imię {imionka[0].capitalize()}")
print(f"Moja znajoma ma na imię {imionka[1].capitalize()}")
print(f"Moja znajoma ma na imię {imionka[2].upper()}")
print(f"Moja znajoma ma na imię {imionka[3].capitalize()}")