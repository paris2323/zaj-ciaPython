import io
from contexlib import redirect_stdout

#
# def a ():
#     return 1
#
# b = a() #uruchamiamy funkcję
# c = a   # c ma ten sam adres co a to idę do a
#
#   # d = c() i wychodzi 1


def get_print_output(tested_func):
    memory_buffer = io.StringIO

    with redirect_stdout(memory_buffer):

        tested_func()

        return memory_buffer.getvalue()

# *args spodziewamy się argumentów ale nie wiemy ile to przy def i przy wywołaniu funkcji wpisujemy i test przejdzie
