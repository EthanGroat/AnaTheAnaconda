#!/usr/bin/python3

# pygame imported as pg in Item.py

from Snake import *


def quit_app():
    pg.quit()
    quit()


class Game:

    def __init__(self):
        pg.init()

        # display:
        self.display_width = 1200
        self.display_height = 600

        self.game_display = pg.display.set_mode((self.display_width,
                                                 self.display_height))
        pg.display.set_caption('Anaconda')

        self.clock = pg.time.Clock()

        self.screen_surf = pg.display.get_surface()
        self.x_mid = self.screen_surf.get_rect().centerx
        self.y_mid = self.screen_surf.get_rect().centery

        # items:
        self.snake = Snake(game_handle=self,
                           head_coordinates=(self.x_mid, self.y_mid, 0),
                           speed=2)

        self.foods = FoodCluster(game_handle=self, foods=5)

        # modes, etc:
        # self.mode = {'move': 'accelerate',
        #              'sticky_rotate': False}

    #   -----------------------------------------------------------------------

    def game_loop(self):

        closed = False

        while not closed:

            # check for close
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    closed = True

            # inputs
            key = pg.key.get_pressed()
            if self.snake.is_alive:
                self.control(self.snake, key)

            # updates
            self.snake.update()
            self.foods.update()

            # display buffer
            self.game_display.fill(black)
            self.snake.show()
            self.foods.show()

            # display frame
            pg.display.update()
            self.clock.tick(48)  # Hobbit framerate

    #   -----------------------------------------------------------------------

    @staticmethod
    def control(snake, key):

        default_boost = 2

        if key[pg.K_LEFT]:
            snake.left()
        if key[pg.K_RIGHT]:
            snake.right()

        if key[pg.K_UP]:
            snake.forward(default_boost*2)
        elif key[pg.K_DOWN]:
            snake.forward(default_boost/2)
        else:
            snake.forward(default_boost)

    #   -----------------------------------------------------------------------


if __name__ == "__main__":

    print('Debug output:')
    a = Game()
    a.game_loop()
    quit_app()
