

prawidlowe = False

while not prawidlowe:
    nazwisko = input('Podaj nazwisko drukowanymi literami: ')

    if nazwisko.isalpha():
        if nazwisko.isupper():
            prawidłowe = True
print('gratulacje, jesteś zarejestrowany')