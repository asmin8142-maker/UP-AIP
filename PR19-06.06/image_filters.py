from PIL import Image

img = Image.open("source.jpg")
pixels = img.load()

width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        tr = min(255, int(0.393*r + 0.769*g + 0.189*b))
        tg = min(255, int(0.349*r + 0.686*g + 0.168*b))
        tb = min(255, int(0.272*r + 0.534*g + 0.131*b))

        pixels[x, y] = (tr, tg, tb)

img.save("filters/sepia.png")