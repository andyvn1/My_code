#!/usr/bin/python3
from os import system, name

# creating a millitary phonetic alphabet
military_phonetic_alphabet = {"A":"ALPHA", "B":"BRAVO", "C":"CHARLIE", "D":"DELTA", "E":"ECHO", "F":"FOXTROX", "G":"GOLF", "H":"HOTEL",  "I":"INDIA", "J":"JULIETTE", "K":"KILO", "L":"LIMA", "M":"MIKE", "N":"NOVEMBER", "O":"OSCAR", "P":"PAPA", 
        "Q":"QUEBEC", "R":"ROMEO", "S":"SIERRA", "T":"TANGO", "U":"UNIFORM", "V":"VICTOR", "W":"WHISKEY", "X":"X-RAY", "Y":"YANKEE", "Z":"ZULU"  }
# creating a police phonetic alphabet
police_phonetic_alphabet = {"A":"ADAM", "B":"BOY", "C":"CHARLES", "D":"DAVID", "E":"EDWARD", "F":"FRANK", "G":"GEORGE", "H":"HENRY", "I":"IDA", "J":"JHON", "K":"KING", "L":"LINCOLN", "M":"MARY", "N":"NORA", "O":"OCEAN", "P":"PAUL", 
        "Q":"QUEEN", "R":"ROBERT", "S":"SAM", "T":"TOM", "U":"UNION", "V":"VICTOR", "W":"WILLIAM", "X":"X-RAY", "Y":"YOUNG", "Z":"ZEBRA" }
#creating a black key and value to add user custom phonetic alphabet
custom_phonetic_alphabet = {}
#clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

choice = ""
while choice  != "EXIT":
    
#user choices with the application
    print()
    print()
    print("1. List of military phonetic alphabet")
    print("2. List of police phonetic alphabet")
    print("3. Add key and value to your own customize phonetic alphabet")
    print("4. List of customize phonetic alphabet -- Only work if you have added key and value to the customize alphabet!!!")
    print("5. Remove letter and its value from custom phonetic alphabet by typing the letter you wich to remove")
    print("6. Get a value for the letter you trying to find on the military phonetic alphabet")
    print("7. Get a value for the letter you trying to find on the police phonetic alphabet")
    print("8. Get a value for the letter you trying to find on the custom phonetic alphabet --If you add to the list in option 3")
    print("9. Exit aplication")
    print()

#Input of the user
    choice = input("Type the number of the selected option or Exit: ").upper()
    clear()

#if, elif, else statement

    if choice == "1":
         for i in military_phonetic_alphabet:
            military_key = i
            military_value = military_phonetic_alphabet[i]
            print(military_key + " = " + military_value)

    elif choice == "2":
        for i in police_phonetic_alphabet:
            police_key = i
            police_value = police_phonetic_alphabet[i]
            print(police_key + " = " + police_value)

    elif choice == "3":
        custom_key_new = input("type the letter you wich to add: ").upper()
        custom_value_new = input("type the name for the value for the previus leter: ").upper()
        custom_phonetic_alphabet[custom_key_new] = custom_value_new
        
        for i in custom_phonetic_alphabet:
            custom_key = i
            custom_value = custom_phonetic_alphabet[i]
            print(custom_key + " = " + custom_value)

    elif choice == "4":
        for i in custom_phonetic_alphabet:
            custom_key = i
            custom_value = custom_phonetic_alphabet[i]
            print(custom_key + " = " + custom_value)

    elif choice == "5":
        letter_remove = input("Type letter you wich to remove with its value: ").upper()
        custom_phonetic_alphabet.pop(letter_remove)
        print("You remove: " + letter_remove)
        for i in custom_phonetic_alphabet:
            custom_remove_letter = i
            custom_remove_value = custom_phonetic_alphabet[i]
            print("You still have:")
            print(custom_remove_letter + " = " + custom_remove_value)


    elif choice == "6":
        get_value_military = input("Please type letter for its value for Military phonmetic alphabet: ").upper()
        print(get_value_military + " = " + military_phonetic_alphabet.get(get_value_military))

    elif choice == "7":
        get_value_police = input("Please type letter for its value for Police phonetic alphabet: ").upper()
        print(get_value_police + " = " + police_phonetic_alphabet.get(get_value_police))


    if choice == "8":
        get_value_custom = input("Please type letter for its value for Custom phonetic alphabet: ").upper()
        try:
             print(get_value_custom + " = " + custom_phonetic_alphabet.get(get_value_custom))
        except:
             print("Please add a letter and its value on option 3")
    
    elif choice == "9":
        break

    else:
        print("Thank you for using The Phonetic Alphabet app")
    



