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

    def __init__(self, game_handle, head_coordinates, speed=2, rotation_speed=6, length=4, separation=16):
        super().__init__(game_handle)
        self.speed = speed
        self.rotation_speed = rotation_speed
        self.separation = separation
        self.items = [Segment(game_handle,
                      color=green,
                      tricoordinates=head_coordinates) for i in range(length)]  # populates the snake segments
        self.Head = self.items[0]

        # load starting position frame stream in queue, interpolating between segment positions for each frame:
        self.frames_per_segment = int(separation/speed)
        self.position_queue = [(head_coordinates[0], head_coordinates[1]+i, 0)
                               for i in range(int(length*self.frames_per_segment))]
        self.boost_multiplier = 1

    def update(self):
        for i in range(self.boost_multiplier):
            self.Head.translate_forward(self.speed)
            self.push_head_position()
            for index, segment in enumerate(self.items):
                segment.queue_card(self.position_queue[index*self.frames_per_segment])  # different positions in the stream
            self.position_queue.pop()
            for food in self.game_handle.foods.items:
                if self.Head.collides_with(food):
                    self.eat(food)
        super().update()

    def push_head_position(self):
        new_coordinate = (self.Head.center[0],
                          self.Head.center[1],
                          self.Head.rotation)
        self.position_queue.insert(0, new_coordinate)

    def forward(self, boost_multiplier=2):
        # boost_multiplier is the multiplier for update iterations per frame,
        # and as such it also speeds up the snake
        self.boost_multiplier = int(boost_multiplier)

    def left(self):
        self.items[0].rotate(self.rotation_speed)

    def right(self):
        self.items[0].rotate(-self.rotation_speed)
        # Note: rotate is not included in update(), so faster boost will not also boost effective rotation speed

    def eat(self, food):
        self.game_handle.foods.remove_into_belly(food)
        self.append(Segment(self.game_handle,
                            tricoordinates=self.items[-1].get_tricoordinates()))
        for i in range(self.frames_per_segment):
            self.position_queue.append(self.items[-1].get_tricoordinates())


class FoodCluster(Fleet):

    def __init__(self, game_handle, foods=3):
        super().__init__(game_handle)
        for food in range(foods):
            self.append(Food(game_handle))

    def remove_into_belly(self, food_bit):
        self.items.remove(food_bit)
        self.append(Food(self.game_handle))  # add another food to screen
