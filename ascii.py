from PIL import Image

# ASCII list of characters to represent the intensity of a pixel
chars = ["@", "#", "X", "%", "?", "*", "+", ";", ":", ",", "."]

# resize the given image to an appropriate width (maintain aspect ratio)
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    new_image = image.resize((new_width, new_height))
    return(new_image)

# convert the image from RGB to grayscale
def grayscale(image):
    gray_image = image.convert("L")
    return(gray_image)

# map each pixel to an ASCII character and convert
def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_characters = "".join([chars[pixel//25] for pixel in pixels])
    return(ascii_characters)


def main(new_width=100):
    image_path = input("Please enter a valid path for an image:\n") # ask for a path from the user
    try:
        image = Image.open(image_path)
    except:
        print(image_path, "is not a valid path.")
        return
    
    # format (string of ASCII characters broken down into lines of length equal to new width)
    new_image_string = pixel_to_ascii(grayscale(resize_image(image)))
    pixel_count = len(new_image_string)
    ascii_image = "\n".join(new_image_string[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # save resulting image
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()