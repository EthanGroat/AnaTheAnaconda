from Item import *


class Fleet:

    def __init__(self, item_list=[]):
        self.items = item_list

    def update(self):
        for item in self.items:
            item.update()

    def add(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            item.show()


class Snake(Fleet):

    def __init__(self, game_handle, head_coordinates, length=4, separation=16):
        super().__init__()
        self.game_handle = game_handle
        self.Head = Segment(game_handle=game_handle, coordinates=head_coordinates)
        self.items.append(self.Head)
        self.separation = separation
        for segment in range(1, length):
            self.items.append(Segment(game_handle,
                                      color=green,
                                      coordinates=head_coordinates))
        # 8 times the speed gives the 16 separation, so need 8 moves per segment
        self.position_queue = [(head_coordinates[0], head_coordinates[1]+i, 0)
                               for i in range(int(length*separation/2))]

    def update(self):
        self.push_head_position()
        index = 0
        for segment in self.items:
            segment.queue_card(self.position_queue[index*8])
            index += 1
        self.position_queue.pop()
        super().update()

    def push_head_position(self):
        new_coordinate = (self.items[0].center[0],
                          self.items[0].center[1],
                          self.items[0].rotation)
        self.position_queue.insert(0, new_coordinate)

    def forward(self, speed=2):
        self.items[0].translate_forward(speed)
        # self.push_head_position()

    def left(self, rotation_speed):
        self.items[0].rotate(rotation_speed)
        # self.push_head_position()

    def right(self, rotation_speed):
        self.items[0].rotate(-rotation_speed)
        # self.push_head_position()

    # more snake stuff
