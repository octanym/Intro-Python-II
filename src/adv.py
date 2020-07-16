from room import Room
from player import Player

# Declare all the rooms

room = {
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

room['outside'].navigation["n"] = room['foyer']
room['foyer'].navigation["s"] = room['outside']
room['foyer'].navigation["n"] = room['overlook']
room['foyer'].navigation["e"] = room['narrow']
room['overlook'].navigation["s"] = room['foyer']
room['narrow'].navigation["w"] = room['foyer']
room['narrow'].navigation["n"] = room['treasure']
room['treasure'].navigation["s"] = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

my_player = Player("Cameron", room['outside'])

print(my_player)

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


# user_is_playing = True

# while user_is_playing:
#   print(my_player.current_room.name)

#   for line in text_wrap.wrap(my_player.current_room.description):
#     print(line)

#   user_input = input("which direction would you like to go?")

#   if user_input in ["n", "e", "s", "w"]
