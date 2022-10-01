import pygame.event

import Game

game = Game.Game(600)
pygame.init()
running = True
while running:
    pressed_keys = pygame.key.get_pressed()
    node = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            node = game.node_at_pos(mouse_pos[0], mouse_pos[1])
            game.choose_action(node, 0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                game.choose_action(node, 1)
            elif event.key == pygame.K_2:
                game.choose_action(node, 2)


    game.draw()
