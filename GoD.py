#!/usr/bin/python3

import sys
import os
from rooms import rooms
from monster_manual import monsters
from time import sleep
import time

# Replace RPG starter project with this code when new instructions are live


def showInstructions():
    # clear the screen, clean the place up a little
    os.system('clear')
    # print a main menu and the commands
    print('''
         Game of Dragons
========================================
This screen will be cleared in 8 seconds.

Commands availble to player:
  go [direction]  get [item]

Possible directions of movement
  [north]   [south]   [east]   [west]
  [downstairs]   [upstairs]   
  [downstairs north end]   [downstairs south end]
  [westnorth]   [westsouth]   [eastnorth]   [eastsouth]
  [northeast]   [northwest]   [southeast]   [southwest]
''')


crsr = "> "


def newPlayer():
    # ask the player for input of their name

    newPlayer = input(
        f"{crsr}Welcome vagabond, what is thy name? \n\n{crsr}").strip().title()
    for l in newPlayer:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)
    # print("\n")


def showStatus(newPlayer):

    # print the player's current status
    print('---------------------------')
    print(f'{newPlayer}, you are in the ' + currentRoom)
    if 'deets' in rooms[currentRoom]:
        print(f'{newPlayer}, you quickly scan the immediate area and see that ' +
              rooms[currentRoom]['deets'])

    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print(f'{newPlayer}, you see a ' + rooms[currentRoom]['item'])
    # print a weapon if there is one
    if "weapon" in rooms[currentRoom]:
        print(f'{newPlayer}, you see a ' + rooms[currentRoom]['weapon'])
    # print a shield if there is one
    if "shield" in rooms[currentRoom]:
        print(f'{newPlayer}, you see a ' + rooms[currentRoom]['shield'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []


# start the player in the Hall
currentRoom = 'Great Hall'

showInstructions()
sleep(3)
os.system('clear')
newPlayer()

# loop forever
while True:

    showStatus(newPlayer)

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
            print('Come on mate, you can\'t go that way!')

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
        # if the item contains a weapon, and they wish to pick it up and equip it
        if "weapon" in rooms[currentRoom] and move[1] in rooms[currentRoom]['weapon']:
            # add item to their right hand
            inventory += [move[1]]
            # display a msg to player to show they now carry the weapon in their strong hand
            print('The ' +
                  move[1] + ' has been retrieved & equipped in your strong hand. You are now a little more dangerous.')
            # delete the item from the room
            del rooms[currentRoom]['weapon']
        # if the item contains a shield, and they wish to pick it up and equip it
        if "shield" in rooms[currentRoom] and move[1] in rooms[currentRoom]['shield']:
            # add item to their off hand
            inventory += [move[1]]
            # display a msg to player to show they now carry the shield in their off hand
            print(' The ' +
                  move[1] + ' has been picked up and equipped in your off hand. You are now a little more safe from attack.')
            # delete the item from the room
            del rooms[currentRoom]['shield']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # # If player enters a room with a monster
    # if 'monster' in rooms[currentRoom]

    # # Define how a player can win
    # if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    #     print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    #     break

    # # If a player enters a room with a monster
    # elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    #     print('A monster has got you... GAME OVER!')
    #     break
