#!/usr/bin/python3
from itertools import count
import random
from re import S
from secrets import choice
import threading
import os

# Replace RPG starter project with this code when new instructions are live
from tabnanny import check


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  Exit --- would exit you out of the game
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("Be aware of the monster in The kitchen")
        print("The only way to by pass the monster is to kill him and put it on the inventory \nfind the item for this and engange in a rock paper scissor match")
    print("---------------------------")

# paper rock and scissor game with the moster


def monster_game():
    fails = 0
    count = 0
    while count < 3:
        computer_choice_list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(computer_choice_list)
        if "sword" in inventory:
            print(
                "You have a sword and can fight the monster on a rock paper scissor match")
            print("1. rock\n2.paper\n3.scissors")
            user_input = input("type rock, paper or scissors: ").lower()
            print(
                f"\n You choice is: {user_input} and the monster choice is: {computer_choice}.")

            if user_input == computer_choice:
                print(f"Both players selected {user_input}. It's a tie!")

            elif user_input == "rock":
                if computer_choice == "scissors":
                    print("Rock smashes scissors! You win and kill the moster!")
                    fails += 1
                    break

                else:
                    print("Paper covers rock! You lose.")
                    count += 1
                    print(f"trys: {count}")

            elif user_input == "paper":
                if computer_choice == "rock":
                    print("Paper covers rock! You win and kill the moster!")
                    fails += 1
                    break

                else:
                    print("Scissors cuts paper! You lose.")
                    count += 1
                    print(f"trys: {count}")

            elif user_input == "scissors":
                if computer_choice == "paper":
                    print("Scissors cuts paper! You win and kill the monster!")
                    fails += 1
                    break

                else:
                    print("Rock smashes scissors! You lose.")
                    count += 1
                    print(f"trys: {count}")

            elif user_input == "exit":
                break

            elif fails == 3:
                print("The monster defeat you... GAME OVER!")
                quit()

        else:
            count = + 3
            print('A monster has got you... GAME OVER!')
            quit()


def riddle_timer():
    print('Game Over!!! Your 3 minutes have expire')
    os._exit(0)


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key',
        'description': ' North of the hall there is a red wall. \n South of the hall there is a kitchen. \n West on the hall there is family pictures on the wall. \n East of the wall there is the dinning room.'
    },
    'Bedroom': {
        'east': 'Pantry',
        'north': 'Bathroom',
        'item': 'sword',
        'description': ' East of the bedroom there is a door to the pantry. \n North of the betroom there is a bathroom. \n West of the bedroom there is a wall where bed is located. \n South of the bedroom there is a wall with a mirror.'
    },
    'Bathroom': {
        'south': 'Bedroom',
        'description': ' South of the bathroom is the bedroom. \n North, East and West is closed by a walls.'
    },

    'Kitchen': {
        'east': 'Garden',
        'north': 'Hall',
        'item': 'monster',
        'description': ' North of the kitchen is the hall. \n East of the kitchen there is a garden \n South and West of the kitchen is close by a wall.'
    },
    'Dining Room': {
        'north': 'Pantry',
        'west': 'Hall',
        'item': 'potion',
        'description': ' West of the dining room there is a hall. \n North of the dining room there is a pantry. \n South and East of the dining room is close walls.'
    },
    'Garden': {
        'west': 'Kitchen',
    },

    'Pantry': {
        'south': 'Dining Room',
        'west': 'Bedroom',
        'item': 'cookie',
        'description': ' West of the pantry there is a door to the bedroom. \n South of the pantry there is a dining room. \n East and North is close by a wall.'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
    # It would break user from the game
    elif move[0] == "exit":
        break

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']

            continue

        if "description" in rooms[currentRoom] and move[1] == "description":
            print(rooms[currentRoom]['description'])

        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # It would break user from the game
    elif move[0] == 'exit':
        break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'monster' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster with rock paper scissor player get 3 try to win one

    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        monster_game()
        print("add monster to the inventory")

    # Bathroom trap logic
    T = threading.Timer(10.0, riddle_timer)

    if currentRoom == 'Bathroom':
        T.start()
        print("You are trap to get out you have three minutes to solve the following riddle using one single word: ")
        while True:
            riddle = input(
                " I am not alive \n but I have \n five fingers \n Whatam I? \n>")
            if riddle.lower() == "glove":
                print('You escape')
                currentRoom = "Bedroom"
                T.cancel()
                break
