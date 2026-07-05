import os
import sys

def simple_dict_program():

    definicje = {}
    while True:

        print("1 - Dodaj definicje do słownika")
        print("2 - Wyszukaj definicje w słowniku")
        print("3 - Usuń definicje ze słownika")
        print("4 - Zakończ program")
        wybor = input("Podaj co chcesz zrobić wybierając numer z menu.")

        if wybor == "1":
            klucz = input("Podaj klucz ktory chcesz dodac do definicjea.")
            definicja = input("Podaj definicje ktora chcesz dodac do definicjea.")
            definicje[klucz] = definicja
            print("Pomyślnie dodano definicje")

        elif wybor == "2":
            klucz = input("Podaj klucz ktory chcesz wyszukać")
            if klucz in definicje:
                print(definicje[klucz])

        elif wybor == "3":
            klucz = input("Podaj klucz ktory chcesz usunać")
            if klucz in definicje:
                del definicje[klucz]
                print("Pomyślnie usunieto")

        elif wybor == "4":
            klucz = input("No to pa... :) ")
            break
        else:
            print("Podano liczbe z poza zakresu menu....")

def main():
    simple_dict_program()

if __name__ == "__main__":
    main()