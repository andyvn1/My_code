#!/usr/bin/python3


# creating a millitary phonetic alphabet
military_phonetic_alphabet = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel",  "I":"India", "J":"Juliett", "K":"Kilo", "L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", 
        "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"X-ray", "Y":"Yankee", "Z":"Zulu"  }
# creating a police phonetic alphabet
police_phonetic_alphabet = {"A":"Adam", "B":"Boy", "C":"Charles", "D":"David", "E":"Edward", "F":"Frank", "G":"George", "H":"Henry", "I":"Ida", "J":"Jhon", "K":"King", "L":"Lincoln", "M":"Mary", "N":"Nora", "O":"Ocean", "P":"Paul", 
        "Q":"Queen", "R":"Robert", "S":"Sam", "T":"Tom", "U":"Union", "V":"Victor", "W":"William", "X":"X-ray", "Y":"Young", "Z":"Zebra" }
#creating a black key and value to add user custom phonetic alphabet
custom_phonetic_alphabet = {}

#user choices with the application
print("1. List of military phonetic alphabet")
print("2. List of police phonetic alphabet")
print("3. Add key and value to your own customize phonetic alphabet")
print("4. List of customize phonetic alphabet -- Only work if you have added key and value to the customize alphabet!!!")
print("5. Get a value for the letter you trying to find on the military phonetic alphabet")
print("6. Get a value for the letter you trying to find on the plice phonetic alphabet")
print()

#Input of the user
choice = input("Type the number of the selected option: ")

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
    custom_key_new = input("type the lettter you wich to add: ")
    custom_value_new = input("type the name for the value for the previus leter: ")
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
    print()
elif choice == "6":
    print()
else:
    print("Run again and *Please type a option between 1-5")
    print("Exiting the application")



