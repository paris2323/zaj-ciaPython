tytuly = ['Skazani na Shawshank', 'Nietykalni', 'Zielona mila', 'Ojciec chrzestny', 'Forrest Gump',\
            'Dwunastu gniewnych ludzi', 'Lot nad kukułczym gniazdem', 'Ojciec chrzestny II', 'Powrót króla'\
            'Pulp Fiction']

rezyser = ['Frank Darabont', 'Olivier Nakache', 'Frank Darabont', 'Francis Coppola', \
        'Robert Zemeckis', 'Sidney Lumet', 'Milos Forman', 'Francis Coppola' \
        'Peter Jackson', 'Quentin Tarantino']

rok_produkcji = ['1994', '2011', '1999', '1972', '1994', '1957', '1975', '1974', '2003', '1994']

baza_filmow = [[tytuly], [rezyser], [rok_produkcji]]

print(baza_filmow)


f1 = ["Nietykalni","Oliver Nakache","2011"]
f2 =["Zielona mila","Frank Darabont","1999"]
baza_filmow = f1 + f2
ww = input("Podaj nazwe: ")

if ww in baza_filmow:
    print(f"{ww} jest już w bazie")
else:
    baza_filmow.append(ww)

print(baza_filmow)



