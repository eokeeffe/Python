import Image

im = Image.open("bluetooth.png")

list = im.histogram()

print list

im.show()