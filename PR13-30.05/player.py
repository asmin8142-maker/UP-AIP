import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(CYAN)
        self.rect = self.image.get_rect(center=(400, 500))
        self.speed = PLAYER_SPEED

    def update(self):
        # Обработка нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed