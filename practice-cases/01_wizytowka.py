import os

def main():
    print("Please enter your name: ")
    name = input()
    print("Please enter your surname: ")
    surname = input()
    print("Please enter your date of birth: ")
    date = input()
    print("Please enter your favorite programming language: ")
    language = input()
    
    age = 2026 - int(date)
    print(age)
    if age < 0: 
        print("Błąd: Rok urodzenia nie może być z przyszłości!")
    wizytowka = f""" 
    +------------------------------------------+ 
    | WIZYTÓWKA PROGRAMISTY | 
    +------------------------------------------+ 
    | Imię i nazwisko : {name} {surname} 
    | Wiek : {age} lat(a) 
    | Ulubiony język : {language} 
    +------------------------------------------+ """ 
    print(wizytowka)        

    
if __name__ == "__main__":
    main()