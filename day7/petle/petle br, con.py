
for x in range(20):
    if x **2 > 280:
        print("Znalazłem element", x)
        break

print("Pierwsza instrukcja po pętli")


#

for w in range (100):
    if w % 7 == 0:
        continue
    else:
        print(w)