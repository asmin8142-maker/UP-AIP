from PIL import Image, ImageDraw, ImageFont

try:
    font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()


def create_meme(image_path, top_text, bottom_text, output_name):
    img = Image.open(image_path)
    width, height = img.size

    draw = ImageDraw.Draw(img)

    # верхний текст
    draw.text((50, 20), top_text, fill="white", font=font)

    # нижний текст
    draw.text((50, height - 60), bottom_text, fill="white", font=font)

    img.save(f"memes/{output_name}.png")
    print(f"{output_name} создан")


# ===== ТУТ ТЫ САМА ВСЁ ВЫБИРАЕШЬ =====

create_meme(
    "source1.jpg",
    "WHEN YOU SEE KIDS OF GUESTS",
    "THEY RUINED ALL YOUR COSMETICS 💀",
    "cosmetics_meme"
)

create_meme(
    "source2.jpg",
    "WHEN YOU WALK INTO YOUR ROOM",
    "AND SEE YOUR COSMETICS DESTROYED BY GUESTS' KIDS 💀",
    "cosmetics_meme2"
)

create_meme(
    "source3.jpg",
    "WHEN EXAM STARTS",
    "I KNOW NOTHING",
    "exam_meme"
)