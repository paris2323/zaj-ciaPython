# fizz buzz

zakres = range(1, 101)
print(zakres)

for liczba in zakres:
    if liczba % 3 == 0:
        print("fizz")
    elif liczba % 5 == 0:
        print("buzz")
    elif liczba % 3 == 0 and liczba % 5 == 0:
        print("fizz buzz")
    else:
        print(liczba)



zakres = range(1, 101)

for liczba in zakres:
    if liczba % 3 == 0:
        print("fizz", end='')
    if liczba % 5 == 0:
        print("buzz", end='')
    if liczba % 3 != 0 and liczba % 5 != 0:
        print(liczba, end='')
    print('\n', end='')