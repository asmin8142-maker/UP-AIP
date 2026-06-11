from PIL import Image, ImageDraw
import random

img = Image.new("RGB", (800, 800), (10, 10, 10))
draw = ImageDraw.Draw(img)

# создаём "комнаты"
for _ in range(25):
    x = random.randint(0, 700)
    y = random.randint(0, 700)
    w = random.randint(50, 150)
    h = random.randint(50, 150)

    draw.rectangle(
        [x, y, x + w, y + h],
        outline=(200, 200, 200),
        width=2
    )

# соединительные линии (коридоры)
for _ in range(15):
    x1 = random.randint(0, 800)
    y1 = random.randint(0, 800)
    x2 = random.randint(0, 800)
    y2 = random.randint(0, 800)

    draw.line((x1, y1, x2, y2), fill=(100, 100, 100), width=2)

img.save("textures/dungeon.png")

print("Dungeon map создан")