#1 napisz program sumujący wszystkie elementy w liscie

lista = [12,45,65,899,12,33,2323]
print(sum(lista))

#2 znajdz najwiekszy / najmniejszy element w liscie

lista = [12,45,65,899,12,33,2323]
print(min(lista))
print(max(lista))

#3 program ktory zmieni zdanie w liste wyrazow

zdanie = "Ala ma kota, kot ma Ale"
lista_wyrazow = zdanie.split()
print(lista_wyrazow)


#4 znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2

lista = ['abc', 'xyz', 'aba', '1221']
for element in lista:
    if element[0] == element[-1]:
        print(f'Te same znaki w wyrazie: {element}')


#5 program znajdujacy wartosci, które wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]
unikatowe = []

for element in lista_a:
    if element not in unikatowe:
        unikatowe.append(element)

print(unikatowe)


#6 program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

lista_b = list(set(lista_b))
print(lista_b)

#7 program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

ings = ['ananas','brokuły','cebula','czosnek','feta','kukurydza','oliwki','kurczak']
ings2 = ['kurczak','czosnek','salami','szynka','oliwki']

for ing in ings:
    if ing in ings2:
        print("True")
