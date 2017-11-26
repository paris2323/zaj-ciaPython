def odwroc_string(zdanie):
    '''Zwraca odwrócony string. Jeśli argument jest pustym stringiem lub None zwraca None
    :param zdanie: Zdanie do odwrócenia
    :return Odwrócone zdanie lub None'''
    if zdanie == "" or zdanie == None:
        return None
    else:
        return zdanie[::-1]

def main():
    imie = "Ala"
    odwr_imie = odwroc_string(imie)
    spr_imie = imie[::-1]

    if odwr_imie == spr_imie:
        print(f"Imię {imie} zostało prawidłowo odwrócone na {odwr_imie}")
    else:
        print(f"Nieprawidłowo {imie} != {odwr_imie}")

if __name__ == '__main__':
    main()