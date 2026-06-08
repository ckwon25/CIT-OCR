from PIL import Image

img = Image.open("/Users/calvin.kwon/Desktop/license.jpeg")

print(img.size)

img.thumbnail((1000, 1000))

img.save("/Users/calvin.kwon/Desktop/license_small.jpeg")

print("done")
