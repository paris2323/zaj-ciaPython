#po podaniu nazwy miesiąca podaj ilość dni

# miesiac = input('podaj nazwe miesiąca: ')
# if  miesiac == 'kwiecien' or miesiac == 'czerwiec'\
#         or 'wrzesień' or miesiac == 'listopad':
#     print()
# elif miesiac == "luty":
#     print()
# else:
#     print()
# import this

miesiac = input("podaj miesiac: ")
if miesiac == "kwiecień" or miesiac == "czerwiec" or miesiac == "wrzesień" or miesiac == "październik":
    print(f'miesiac {miesiac} ma 30 dni')
elif miesiac == "luty":
    print('luty ma 30 dni')
else:
    print(f"miesiac {miesiac} ma 31 dni")
