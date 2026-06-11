import pygame
import random
import math

# --- НАСТРОЙКИ (Settings) ---
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (5, 5, 10)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VOID INVADERS")
clock = pygame.time.Clock()

font_ui = pygame.font.SysFont('Arial', 24)
font_big = pygame.font.SysFont('Arial', 60, bold=True)

# --- КЛАССЫ ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 255, 255), [(25, 0), (50, 50), (0, 50)])
        self.rect = self.image.get_rect(center=(WIDTH//2, 500))
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= 8
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH: self.rect.x += 8
    def shoot(self):
        b = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(b); bullets.add(b)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((6, 15)); self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        self.rect.y -= 12
        if self.rect.bottom < 0: self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.rect = self.image.get_rect(x=random.randint(0, WIDTH-40), y=-50)
        self.timer = random.randint(0, 100)
    def update(self):
        self.rect.y += self.speed
        self.timer += 0.1
        pulse = abs(math.sin(self.timer)) * 100 + 155
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (pulse, 0, 50), (20, 20), 20)
        pygame.draw.circle(self.image, (255, 255, 255), (20, 20), 5)
        if self.rect.top > HEIGHT: self.kill()

# --- ИНИЦИАЛИЗАЦИЯ ИГРЫ ---
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

score, lives, state = 0, 3, "MENU"
enemy_speed, spawn_rate = 5, 20
stars = [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(150)]

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if state == "MENU" and event.key == pygame.K_RETURN: state = "PLAYING"
            if state == "PLAYING" and event.key == pygame.K_SPACE: player.shoot()
            if state == "GAMEOVER" and event.key == pygame.K_RETURN:
                score, lives, enemy_speed, spawn_rate = 0, 3, 5, 20
                enemies.empty(); bullets.empty(); state = "PLAYING"

    screen.fill(BG_COLOR)
    # Анимация звезд
    for s in stars:
        s[1] = (s[1] + 2) % HEIGHT
        pygame.draw.circle(screen, (200, 200, 255), s, random.randint(1, 2))

    if state == "PLAYING":
        if random.randint(1, max(5, spawn_rate)) == 1:
            e = Enemy(enemy_speed)
            all_sprites.add(e); enemies.add(e)
        all_sprites.update()
        
        if pygame.sprite.groupcollide(enemies, bullets, True, True): score += 10
        if pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
            if lives <= 0: state = "GAMEOVER"
        
        all_sprites.draw(screen)
        ui = font_ui.render(f'Score: {score}  Lives: {lives}', True, (255, 255, 255))
        screen.blit(ui, (10, 10))
    
    elif state == "MENU":
        text = font_big.render("VOID INVADERS", True, (150, 0, 255))
        screen.blit(text, text.get_rect(center=(WIDTH // 2, 250)))
        hint = font_ui.render("Press ENTER to Begin", True, (255, 255, 255))
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2, 320)))
    
    elif state == "GAMEOVER":
        text = font_big.render("YOU WERE CONSUMED", True, (255, 0, 0))
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        score_text = font_ui.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, score_surf := score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))

    pygame.display.flip()
pygame.quit()