from enum import Enum

class Direction(Enum):
    # syntax is MEMBER_NAME = value
    # name can be accessed using <thing>.name
    # value can be accessed using <thing>.value
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"





class Player:

    def move(self, *, direction: Direction):
        if not isinstance(direction, Direction):
            raise TypeError('direction must be of type Direction')

        print("moving in direction: {}".format(direction.value))
        
    # the following is just an example of type hinting in practice
    # see PEP484 for more details
    def plusOne(self, value: int) -> int:
        return value + 1


