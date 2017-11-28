file_path = "dane.txt"

try:
    with open(file_path, "w") as file:
        print(file.read())
except FileNotFoundError:
    print("podny plik nie istnieje")
except Exception as e:
    print("Ups, nastąpił jakiś błąd.", e)
finally:
    print('ta funkcja zawsze się wykona')