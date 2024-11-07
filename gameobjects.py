from random import randint

import pygame


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

GRID_SIZE = 20


class GameObject:

    def __init__(self, position, body_color):
        self.position = position
        self.body_color = body_color

    def draw(self, screen):
        rect = pygame.Rect(self.position[0], self.position[1], 20, 20)
        pygame.draw.rect(screen, self.body_color, rect)


class Apple(GameObject):

    def __init__(self):
        self.body_color = (255, 0, 0)
        self.randomize_position()
        super().__init__(self.position, self.body_color)

    def randomize_position(self):
        x = randint(0, 32) * 20
        y = randint(0, 24) * 20
        self.position = (x, y)
        return (x,y)


class Snake(GameObject):

    def __init__(self):
        self.length = 1
        self.position = [(640 // 2, 480 // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = (0, 255, 0)
        super().__init__(self.position, self.body_color)

    def update_direction(self, next_direction):
        self.direction = next_direction

    def move(self):
        head = self.get_head_position()
        new_pos = (head[0] + (20 * self.direction[0]), (head[1] + 20 * self.direction[1]))
        if new_pos[0] > 640:
            new_pos = (abs(new_pos[0]-640), new_pos[1])
        elif new_pos[0] < 0:
            new_pos = (abs(640-new_pos[0]), new_pos[1])
        elif new_pos[1] > 480:
            new_pos = (new_pos[0], abs(new_pos[1]-480))
        elif new_pos[1] < 0:
            new_pos = (new_pos[0], abs(480-new_pos[1]))
        if len(self.position) >= self.length:
            self.position.pop()
        if new_pos in self.position:
            self.reset()
        else:
            self.position.insert(0, new_pos)


    def draw(self, screen):
        for cord in self.position:
            rect = pygame.Rect(cord[0], cord[1], 20, 20)
            pygame.draw.rect(screen, self.body_color, rect)

    def get_head_position(self):
        return self.position[0]

    def reset(self):
        self.__init__()
