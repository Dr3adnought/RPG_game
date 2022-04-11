#!/usr/bin/python3

from rooms import rooms

# Replace RPG starter project with this code when new instructions are live


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]

Possible directions of movement
  [north]
  [south]
  [east]
  [west]
  [downstairs]
  [upstairs]
  [downstairs north end]
  [downstairs south end]
  [westnorth]
  [westsouth]
  [eastnorth]
  [eastsouth]
  [northeast]
  [northwest]
  [southeast]
  [southwest]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    if 'deets' in rooms[currentRoom]:
        print('You quickly scan the immediate area and see that ' +
              rooms[currentRoom]['deets'])

    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    # print a weapon if there is one
    if "weapon" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['weapon'])
    # print a shield if there is one
    if "shield" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['shield'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []


# start the player in the Hall
currentRoom = 'Great Hall'

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

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
