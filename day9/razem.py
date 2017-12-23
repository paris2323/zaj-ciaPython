from day9.restauracje import Rest
from day9.pracownicy import Workers_Restaurant


restauracja1 = Rest("Pueblo","meksykańska")
restauracja1.describe_rest()
restauracja1.open_rest()
restauracja1.number_served = 23
restauracja1.set_number_served()

restauracja2 = Rest("Lao Thai","tajska")
restauracja2.describe_rest()
restauracja2.open_rest()


user1 = Workers_Restaurant("Anna","Gul","kelnerka")
user1.describe_worker()


user2 = Workers_Restaurant("Janek","Nowak","szef zmiany")
user2.describe_worker()



