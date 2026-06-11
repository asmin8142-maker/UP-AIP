from PIL import Image, ImageEnhance

img = Image.open("source.jpg")

img = ImageEnhance.Color(img).enhance(3)
img = ImageEnhance.Contrast(img).enhance(2)
img = ImageEnhance.Sharpness(img).enhance(4)

img.save("memes/deep_fried.png")