# daj listę zawierające unikalne wartości

lista_a = [10,20,332,23,234,10,435,35,234, 20, 4938, 435, 23]

unikalne = []

for element in lista_a:
    if element not in unikalne:
        unikalne.append(element)

print(unikalne)
