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
                                      coordinates=(head_coordinates[0],
                                                   head_coordinates[1] + separation*segment)))
        # 8 times the speed gives the 16 separation, so need that many moves per segment to track the next segment
        self.move_queue = ['u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2',
                           'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2',
                           'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2',
                           'u2']

    def update(self):
        index = 0
        for segment in self.items:
            segment.queue_card(self.move_queue[index*8])
            index += 1
        self.move_queue.pop()

    def forward(self, speed=2):
        # self.items[0].translate_forward(speed)
        self.move_queue.insert(0, 'u2')

    def left(self, rotation_speed):
        # self.items[0].rotate(rotation_speed)
        self.move_queue.insert(0, 'l5')

    def right(self, rotation_speed):
        # self.items[0].rotate(-rotation_speed)
        self.move_queue.insert(0, 'r5')

    # more snake stuff
