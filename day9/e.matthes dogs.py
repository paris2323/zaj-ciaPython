class Dog(object):

    def __init__(self,name,age):
        """"Tworzy instancję obiektu typu pies
        :param imię: str - imię
        :param age: int - wiek"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.capitalize()} teraz siedzi.")

    def roll_over(self):
        print(f"{self.name.capitalize()} teraz położył się na plecy.")


my_dog = Dog("Pako",2)
print(f"Mój pies ma na imię {my_dog.name.capitalize()}.")
print(f"Mój pies ma {my_dog.age} lata.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Atos",12)
print(f"Twój pies ma na imię {your_dog.name.capitalize()}.")
your_dog.sit()