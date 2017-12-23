from day9.restauracje import *

class Workers_Restaurant:
    def __init__(self,first_name,last_name,position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.rest = None

    def describe_worker(self):
        print(f"{self.first_name.title()} {self.last_name.title()} pracuje na stanowisku: {self.position}.")



