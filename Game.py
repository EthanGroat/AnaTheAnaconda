# import pygame as pg  # not needed because it is imported in Item.py

from Item import *
from Snake import *


def quit_app():
    pg.quit()
    quit()


class Game:

    def __init__(self):
        pg.init()

        self.display_width = 1200
        self.display_height = 600

        self.game_display = pg.display.set_mode((self.display_width, self.display_height))
        pg.display.set_caption('Yeah Toast!')

        self.clock = pg.time.Clock()

        self.screen_surf = pg.display.get_surface()
        self.x_mid = self.screen_surf.get_rect().centerx
        self.y_mid = self.screen_surf.get_rect().centery

        # item declarations
        # self.HappyBread = NewtonianItem(game_handle=self, sprite='resources/HappyBread_wT.png',
        #                                 coordinates=(self.x_mid, self.y_mid))
        # self.Toaster = Item(game_handle=self, sprite='resources/Toaster.png',
        #                     coordinates=(256, 288))
        # self.fleet = Fleet([self.Toaster, self.HappyBread])

        self.snake = Snake(game_handle=self, head_coordinates=(self.x_mid, self.y_mid))

        self.mode = {'move': 'accelerate',
                     'sticky_rotate': False}

        # self.events = []

    #   -----------------------------------------------------------------------

    def game_loop(self):

        closed = False

        print('Debug output:')

        while not closed:

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    closed = True

            key = pg.key.get_pressed()

            # controls go here
            self.control(self.snake, key)

            self.snake.update()

            self.game_display.fill(black)
            self.show_all_items()

            pg.display.update()
            self.clock.tick(48)  # Hobbit framerate

    #   -----------------------------------------------------------------------

    # these guys could probably go into item and fleet, respectively

    def show(self, item):
        self.game_display.blit(item.rotated, item.rect)

    def show_all_items(self):
        for item in self.snake.items:
            self.show(item)

    #   -----------------------------------------------------------------------

    @staticmethod
    def control(item, key,
                forward_speed=2.4,
                rotation_sensitivity=5):

        s = forward_speed

        if key[pg.K_UP]:
            item.forward(s*2)
        elif key[pg.K_DOWN]:
            item.forward(s*0.5)
        else:
            item.forward(s)

        if key[pg.K_LEFT]:
            item.left(rotation_sensitivity)
        if key[pg.K_RIGHT]:
            item.right(rotation_sensitivity)

    #   -----------------------------------------------------------------------


if __name__ == "__main__":
    a = Game()
    a.game_loop()
    quit_app()
