import pygame as pg 
import sys
from settings import *
from map import *
from player import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES) # Screen to render resolution
        self.clock = pg.time.Clock() # Set framerate?
        self.delta_time = 1
        self.new_game() #   Call newgame from main application constructor

    def new_game(self):
        self.map = Map(self)    # create instance of map class
        self.player = Player(self)

    def update(self):
        self.player.update()
        pg.display.flip()    # Refresh screen
        # Display fps in window caption
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def draw(self):
        self.screen.fill('black') # Paint screen black after each duration
        self.map.draw()
        self.player.draw()

    # Check for closing window or if esc is pressed
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            

    # Run method where the main loop of the game will be
    def run(self):
        while True: # Call update and draw methods
            self.check_events()
            self.update()
            self.draw()
            

# Create instance of game and call run method
if __name__ == '__main__':
    game = Game()
    game.run()