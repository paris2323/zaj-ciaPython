# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32


stopnie = int(input("podaj ilość stopni: "))
jednostka = input("C czy F: ")
if jednostka.upper() == "C":
    stopnieF = stopnie * (9 / 5) + 32
    typ = "skali farenhaita"
    print(f"Temperatura w {typ} to {stopnieF} stopni.")
if jednostka.upper() == "F":
    stopnieC = (stopnie - 32) * (5/9)
    typ = "skali celsjusza"
    print(f"Temperatura w {typ} to {stopnieC} stopni.")

# Komentarz Arka:
# Co do temperatury - czy musimy sprawdzać czy stopnie to C i F?
# Skoro jedno jest prawdziwe to na pewno nie drugi przypadek - tutaj if-elif





