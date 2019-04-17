from Item import Segment


class Fleet:

    def __init__(self, item_list=[]):
        self.items = item_list

    def update(self):
        for item in self.items:
            item.update()

    def add(self, item):
        self.items.append(item)


class Snake(Fleet):

    def __init__(self, game_handle, head_coordinates, length=4):
        super().__init__()
        self.game_handle = game_handle
        self.Head = Segment(game_handle=self, coordinates=head_coordinates)
        self.items.append(self.Head)
        # for segment in range(length):
        #     self.items.add(Segment(self, (head_coordinates[0], head_coordinates[1]+16)))

    def forward(self, speed):
        self.items[0].translate_forward(speed)

    def left(self, rotation_speed):
        self.items[0].rotate(rotation_speed)

    def right(self, rotation_speed):
        self.items[0].rotate(-rotation_speed)


    # more snake stuff
