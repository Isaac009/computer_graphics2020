import sys
import pygame
import pygameMenu
from random import randint
from random import randrange
from pygame.locals import *
from pygameMenu.locals import*
#  create the menu 
class GameMenu():
    # this will used on click's 
    def test(self):
        print('test')
    # this will create the menu with some features
    def my_menu_game(self):
        self.my_menu_game = pygameMenu.Menu(get_display,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   dopause=False,
                                   menu_color=(0, 10, 176),  # Background color
                                   menu_color_title=(0, 76, 76),
                                   menu_height= 240,
                                   menu_width=320,
                                   onclose=pygameMenu.events.DISABLE_CLOSE,
                                   option_shadow=True,
                                   option_shadow_position=pygameMenu.locals.POSITION_SOUTHEAST,

                                   title='Help',
                                   window_height=480,
                                   window_width=640
                                        )
        # add some items on menu 
        self.my_menu_game.add_option('Test!', self.test)
        self.my_menu_game.add_selector('Select', [('eazy', 'EASY'),
                                                     ('medium', 'MEDIUM'),
                                                     ('hard', 'HARD')],
                                onreturn = False,
                                onchange = self.test)
        self.my_menu_game.add_option('Exit', self.test)



        # Loop the game and get menu events
        while True:
            # clock count
            clock.tick(60)
            # events for menu 
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # create menu
            self.my_menu_game.mainloop(events)

            # the flip display function 
            pygame.display.flip()


# init the pygame 
pygame.init()

# default pygame init
get_display=pygame.display.set_mode((640,480))
pygame.display.set_caption("My Menu")
clock = pygame.time.Clock()

# create the menu
game_menu = GameMenu()
game_menu.my_menu_game() 