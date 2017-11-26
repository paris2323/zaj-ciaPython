zdanie = input ('podaj jakieś zdanie: ')

samogloski = 0
spolgloski = 0

lista_samoglosek = 'aąeęiouyó'

for litera in zdanie:
    if litera.isalpha():
        if litera in lista_samoglosek:
            samogloski += 1
        else:
            spolgloski += 1

print(f"Samogłoski: {samogloski}, społgłoski: {spolgloski}")