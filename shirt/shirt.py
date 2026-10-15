import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

exts = (".jpg", ".jpeg", ".png")
input_file = sys.argv[1].lower()
output_file = sys.argv[2].lower()

if not input_file.endswith(exts) or not output_file.endswith(exts):
    sys.exit("Invalid input")

ext1 = input_file.split(".")[-1]
ext2 = output_file.split(".")[-1]

if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    user_photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    fitted_photo = ImageOps.fit(user_photo, shirt.size)

    fitted_photo.paste(shirt, (0, 0), shirt)

    fitted_photo.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
