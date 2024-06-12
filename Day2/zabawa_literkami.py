#podsawowe jakieś takie
imionko = "Wiktoria"
print("Hej "+ imionko + " rozwal mi życie")

imionko2 = "szmata "
print("Moja była z konstantynowa to: " + imionko2.lower() + imionko2.upper() + imionko2.capitalize())

#Używanie apostrofów i innych f stringów
cytat = "'Show me that you really care. That you're really here. Show me that you'rе gonna stay. On my worst days. Hold me like you'll nevеr leave.'"
print("Girl In Red w utworze I'll call you mine: " + cytat)

ulub_artysta = "Girl In Red "
tytul = "I'll call You Mine"
print(f"{ulub_artysta} w utworze {tytul}: {cytat}")

#stripowanie ciągu znaków
imionko3 = "\tWiktoria Roksana Kowalska\t"
print(f"{imionko3} imionko bez usuwania znaków")
print(f"{imionko3.lstrip()} imionko lstrip")
print(f"{imionko3.rstrip()} imionko rstrip")
print(f"{imionko3.strip()} imionko strip")

#usuwanie suffixu
pliczek = "uwu.txt"
print(pliczek.removesuffix(".txt"))