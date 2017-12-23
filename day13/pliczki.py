import os, shutil
# print(shutil.disk_usage("./"))

pliki = os.listdir("PycharmProjects\zaj-ciaPython\day12\kalkulator_testy.py")

for plik in pliki:
    print(plik)

os.walk()

