from room import Room
from player import Player
import textwrap

# Declare all the rooms

location = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

location['outside'].navigation["n"] = location['foyer']
location['foyer'].navigation["s"] = location['outside']
location['foyer'].navigation["n"] = location['overlook']
location['foyer'].navigation["e"] = location['narrow']
location['overlook'].navigation["s"] = location['foyer']
location['narrow'].navigation["w"] = location['foyer']
location['narrow'].navigation["n"] = location['treasure']
location['treasure'].navigation["s"] = location['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

my_player = Player("Cameron", location['outside'])

# print(my_player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# print(my_player.current_room.description)

user_is_playing = True

while user_is_playing:
    print(my_player.current_room.name)

    for line in textwrap.wrap(my_player.current_room.description, 12):
        print(line)

    player_input = input("Where should we go? n? s? e? or w?")

    if player_input in ["n", "e", "s", "w"]:
        my_player.explore(player_input)
    else:
        print("You exited the game")
        break
