import pygame
import random
import easygui

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("The game is Til")
icon = pygame.image.load("img/aimLogo.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
hit_image = pygame.image.load("img/hit.png")  # Загрузите изображение, которое будет отображаться при попадании
current_image = target_image  # Текущее изображение для отображения

target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

hits = 0
misses = 0
speed = 0.05
direction_x = 1 if random.random() < 0.5 else -1  # Случайное начальное направление
direction_y = 1 if random.random() < 0.5 else -1  # Случайное начальное направление

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                speed += 0.05
                current_image = hit_image if current_image == target_image else target_image  # Переключение изображения
                if hits % 3 == 0:  # После 3 попаданий, спросить у пользователя, хочет ли он продолжить
                    message = f"Вы попали в цель 3 раза! У вас {hits} попаданий и {misses} промахов. Хотите продолжить?"
                    continue_game = easygui.ynbox(message, choices=('Да', 'Нет'))
                    if not continue_game:
                        running = False
            else:
                misses += 1
    target_x += direction_x * speed
    target_y += direction_y * speed
    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        direction_x *= -1
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        direction_y *= -1
    screen.blit(current_image, (target_x, target_y))
    pygame.display.set_caption(f"The game is Til - Попаданий: {hits}, Промахов: {misses}")  # Обновите заголовок окна с текущим счетом
    pygame.display.update()

pygame.quit()
