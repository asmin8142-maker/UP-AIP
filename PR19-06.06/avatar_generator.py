from PIL import Image, ImageDraw
import random

size = 500


# =========================
# 1. CYBERPUNK AVATAR
# =========================
def cyberpunk_avatar():
    img = Image.new("RGB", (size, size), (10, 10, 25))
    draw = ImageDraw.Draw(img)

    # неоновая рамка
    draw.rectangle(
        (40, 40, size-40, size-40),
        outline=(0, 255, 255),
        width=6
    )

    draw.rectangle(
        (80, 80, size-80, size-80),
        outline=(255, 0, 255),
        width=3
    )

    # центральный круг
    draw.ellipse(
        (150, 150, 350, 350),
        outline=(255, 255, 0),
        width=5
    )

    img.save("avatars/avatar_cyberpunk.png")


# =========================
# 2. GRADIENT ICON AVATAR
# =========================
def gradient_avatar():
    img = Image.new("RGB", (size, size))
    pixels = img.load()

    c1 = (255, 0, 150)
    c2 = (0, 200, 255)

    for x in range(size):
        for y in range(size):
            r = int(c1[0] * (x/size) + c2[0] * (1-x/size))
            g = int(c1[1] * (x/size) + c2[1] * (1-x/size))
            b = int(c1[2] * (x/size) + c2[2] * (1-x/size))
            pixels[x, y] = (r, g, b)

    draw = ImageDraw.Draw(img)

    # белый символ (простая эмблема)
    draw.ellipse((170, 170, 330, 330), outline="white", width=6)

    img.save("avatars/avatar_gradient.png")


# =========================
# 3. RPG GUILD ICON
# =========================
def rpg_avatar():
    img = Image.new("RGB", (size, size), (30, 20, 10))
    draw = ImageDraw.Draw(img)

    # щит
    shield = [(250, 80), (380, 180), (340, 380), (160, 380), (120, 180)]
    draw.polygon(shield, outline=(255, 215, 0), fill=(60, 40, 10))

    # меч
    draw.line((250, 120, 250, 350), fill="silver", width=6)

    draw.line((230, 200, 270, 200), fill="silver", width=4)

    img.save("avatars/avatar_rpg.png")


# =========================
# 4. MINIMAL ICON
# =========================
def minimal_avatar():
    img = Image.new("RGB", (size, size), (240, 240, 240))
    draw = ImageDraw.Draw(img)

    colors = [
        (0, 0, 0),
        (50, 50, 50),
        (120, 120, 120)
    ]

    # простая геометрия
    draw.ellipse((120, 120, 380, 380), fill=random.choice(colors))

    draw.rectangle((200, 200, 300, 300), fill=(255, 255, 255))

    img.save("avatars/avatar_minimal.png")


# =========================
# RUN ALL
# =========================
cyberpunk_avatar()
gradient_avatar()
rpg_avatar()
minimal_avatar()

print("Красивые аватарки созданы")