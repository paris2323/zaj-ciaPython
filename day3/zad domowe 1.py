# # sprawdź czy jest wygrana w kółko i krzyżyk
# # input: string 9 znaków x,o,n
# #znaki oznaczają pozycje wierszami od górnego
#
#
# # jeśli chodzi o kółko i krzyżyk w zupełności da się to zrobić tylko ze stringami; mamy w sumie dwie możliwości
# #  - albo gra jest wygrana albo nierozstrzygnięta, jeśli jest wygrana to wygrywa X lub O.
# # String wejściowy "XOXONXOOX" przekłada się na grę:
# # XOX
# # ONX
# # OOX
#
string = input("Podaj 9 znaków: ")
if string[:3] == "XXX" or string[3:6] == "XXX" or string[-3:] == "XXX" or string[0:9:3] == "XXX" or \
    string[1:9:3] == "XXX" or string[2:9:3] == "XXX" or string[0:9:4] == "XXX" or string[2:8:2] == "XXX":
    print('wygrywają X')
elif string[:3] == "000" or string[3:6] == "000" or string[-3:] == "000" or string[0:10:3] == "000" or \
string[1:9:3] == "000" or string[2:9:3] == "000" or string[0:9:4] == "000" or string[2:8:2] == "000":
    print('wygrywają 0')
else:
    print('przegrana')

# kółko i krzyżyk - obecnie,w najgorszym przypadku trzeba 16 razy sprawdzić czy jest wygrana
# - da radę zrobić tak aby było 8 sprawdzeń (+2?)

















