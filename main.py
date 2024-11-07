import pygame
import gameobjects
# Инициализировать библиотеку Pygame.


pygame.init()

# Создать окно размером 800x600 точек (или пикселей).
screen = pygame.display.set_mode((640, 480))
# Задать окну заголовок.
pygame.display.set_caption('Змейка!')


running = True
snake = gameobjects.Snake()
apple = gameobjects.Apple()
clock = pygame.time.Clock()

# Описание главного цикла игры.
# Этот цикл работает до тех пор, пока пользователь не закроет окно.
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.update_direction(gameobjects.LEFT)
            if event.key == pygame.K_UP:
                snake.update_direction(gameobjects.UP)
            if event.key == pygame.K_RIGHT:
                snake.update_direction(gameobjects.RIGHT)
            if event.key == pygame.K_DOWN:
                snake.update_direction(gameobjects.DOWN)
    if snake.get_head_position() == apple.position:
        snake.length += 1
        new_apple_pos = apple.randomize_position()
        while new_apple_pos in snake.position:
            new_apple_pos = apple.randomize_position()
    apple.draw(screen)
    snake.draw(screen)
    snake.move()
    pygame.display.update()
    clock.tick(20)



# Деинициализирует все модули pygame, которые были инициализированы ранее.
pygame.quit()