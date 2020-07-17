# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.navigation = {
            "n": n_to,
            "e": e_to,
            "s": s_to,
            "w": w_to
        }

# what if each room just had a navigation dictionary?
# class Room:
#   def __init__(self, name, description, n_to=None, s_to= None, e_to=None, w_to=None):
#     self.name = name
#     self.description = description
#     self.navigation = {
#       "n": n_to,
#       "e": e_to,
#       "s": s_to,
#       "w": w_to
#     }
# then on adv.py
# we would call the connections like so --> room['outside'].connections["n"] = room['foyer']
