from Item import *


class Fleet:

    def __init__(self, game_handle=None, item_list=[]):
        self.game_handle = game_handle
        self.items = item_list

    def update(self):
        for item in self.items:
            item.update()

    def append(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            item.show()


class Snake(Fleet):

    def __init__(self, game_handle, head_coordinates, length=4, separation=16):
        super().__init__(game_handle)
        self.separation = separation
        self.items = [Segment(game_handle,
                      color=green,
                      coordinates=head_coordinates) for i in range(length)]
        self.Head = self.items[0]
        # 8 times the speed gives the 16 separation, so need 8 moves per segment
        self.position_queue = [(head_coordinates[0], head_coordinates[1]+i, 0)
                               for i in range(int(length*separation/2))]

    def update(self):
        self.push_head_position()
        for index, segment in enumerate(self.items):
            segment.queue_card(self.position_queue[index*8])
        self.position_queue.pop()
        for food in self.game_handle.foods.items:
            if self.Head.collides_with(food):
                self.game_handle.foods.remove_into_belly(food)
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


class FoodCluster(Fleet):

    def __init__(self, game_handle, foods=3):
        self.game_handle = game_handle
        self.items = []
        for food in range(foods):
            self.append(Food(game_handle))

    def remove_into_belly(self, food_bit):
        self.items.remove(food_bit)
        self.append(Food(self.game_handle))  # add another food to screen
