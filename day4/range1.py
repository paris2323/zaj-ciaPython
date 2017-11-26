zakres = range(4)
print(zakres) # poda nam te wartości od 1 do miliona ale dopiero jak będziemy go o to prosić, czyli nie rezerwuje pamięci 

inty = [1,2,3,4]
print(inty)   # pamięć na 4 elementy już zarezerwowana

# policz samogloski i spolgloski
zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samoglosek = 'aeiouyąęó'
for litera in zdanie:
    if litera in lista_samoglosek:
        samogloski += 1
    else:
        spolgloski += 1
print(f"liczba samogłosek: {samogloski}, liczba spółgłosek: {spolgloski}")

