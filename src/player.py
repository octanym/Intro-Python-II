# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    # method uses attr as an element in equivocate rather than storing as a value
    def explore(self, direction):
        if self.current_room.navigation[direction] is not None:
            self.current_room = self.current_room.navigation[direction]
        else:
            print(f"It seems we've come to an impasse...")
