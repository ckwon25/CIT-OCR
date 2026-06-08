from PIL import Image

img = Image.open("IMG_8708.jpeg")

print("Original:", img.size)

img.thumbnail((1200, 1200))

img.save("IMG_8708_small.jpeg", quality=85)

print("New:", img.size)
