#!/usr/bin/python3

papaya = {"chemistry":"[phytochemicals, carotenoid, polyphenols]",
        "distribution_habitat" : "tropical america",
        "sexes":"[male, female, hermaphrodite]",
        "toxity":"yes",
        "uses" : "[papaya juice, papaya jam]"
        }

print("papaya: ")
print()
print(papaya)
print()
print()

print("papaya keys")
print(papaya.keys())
print()

print("papaya values")
print(papaya.values())
print()
print()

print("1. removing key with value")
print("2. new key and value to add")
print("3. getting keys and its value on the list")
print()

selection = input("type the number of wich one you wish to select ")

if(selection == "1"):
    word_pop = input("What key with their  value you wich to remove: ")
    papaya.pop(word_pop)
    print("papaya: ")
    print()
    print(papaya)
    print()
    print("1. removing key with value")
    print("2. new key and value to add")
    print("3. getting keys and its value on the list")
    print()
    selection = input("type the number of wich one you wish to select ")   

if(selection == "2"):
    new_key = input("Write new key you would like to add: ")
    new_value = input("Write new valye for the key previusly added: ")
    papaya[new_key] = new_value
    print("papaya: ")
    print()
    print(papaya)
    print()
    print("1. removing key with value")     
    print("2. new key and value to add")                        
    print("3. getting keys and its value on the list")                                                          
    print()                                                                                                                         
    selection = input("type the number of wich one you wish to select ") 

if(selection == "3"):
    get_key_with_value = input("Write a key you whitch to get: ")
    papaya.get(get_key_with_value)
    print("1. removing key with value")                                                                                             
    print("2. new key and value to add")                                                                                               
    print("3. getting keys and its value on the list")                                                                              
    print()                                                                                                                         
    selection = input("type the number of wich one you wish to select ")


else:
    print("input should be 1-3")

