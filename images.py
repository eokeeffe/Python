import Image
im = Image.open("vlc.png")

print im.format, im.size, im.mode

im.show()