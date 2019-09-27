from Item import *


class Segment(Item):

    def __init__(self, game_handle, color=green, tricoordinates=(0, 0, 0), width=26):
        super().__init__(game_handle, sprite=None,
                         coordinates=(tricoordinates[0], tricoordinates[1]),
                         width=width, color=color)
        self.rotate(tricoordinates[2])

    def get_tricoordinates(self):
        return self.center[0], self.center[1], self.rotation

    def queue_card(self, tricoordinates=(0, 0, 0)):  # third coordinate is rotation
        self.teleport(tricoordinates[0], tricoordinates[1], reset_rotation=True)
        self.rotate(tricoordinates[2])


class Food(AcceleratingItem):

    def __init__(self, game_handle):
        super().__init__(game_handle, sprite="resources/bluefood.png", width=9)
        # rand = random()
        self.teleport(randint(0, game_handle.display_width), randint(0, game_handle.display_height))
