from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game    # instance of game
        self.x, self.y = PLAYER_POS    # pos
        self.angle = PLAYER_ANGLE    # angle of direction

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time  # player speed in dt
        speed_sin = speed * sin_a    # precalculate player speed
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()    # calc increments in dx and dy
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)    # apply received increments
        

        if keys[pg.K_LEFT]:    # calc player direction
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau    # tau = 2*pi

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):    # player and line direction of movement (facing)
        pg.draw.line(self.game.screen, 'yellow', (self.x * 70, self.y * 70),
                    (self.x * 70 + WIDTH * math.cos(self.angle),
                    self.y * 70 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 70, self.y * 70), 15)

    def update(self):
        self.movement()  # call movement through update method

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)