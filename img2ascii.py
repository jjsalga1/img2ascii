import PIL
from PIL import Image, ImageOps

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image according to a new width
def resize_image(image, new_width=150) -> Image:
    width, height = image.size
    ratio = height / width / 2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# convert each pixel to grayscale
def grayscale(image, invert=False) -> Image:
    grayscale_image = image.convert("L")
    if invert:
        grayscale_image = ImageOps.invert(grayscale_image)
    return grayscale_image


# convert pixels to a string of ascii characters
def pixels_to_ascii(image) -> str:
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(path, new_width=150):
    # path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)

    except:
        print(path, " is not a valid pathname to an image.")
        return None

    # convert image to ascii
    new_image_data = pixels_to_ascii(grayscale(resize_image(image), invert=False))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open(path[11:]+"_ascii_image.txt", "w") as f:
        f.write(ascii_image)


# run program
if __name__ == "__main__":
    for num in range(1, 1209):
        number = "{i:04d}".format(i=num)
        filename = "frames-may/out"+number+".png"
        main(filename)


