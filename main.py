from PIL import Image
import sys

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  # Adjust for aspect ratio
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")  # Convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  # Map pixel value to ASCII character
    return ascii_str

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)

    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    print(ascii_img)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ascii_image.py <image_path> [new_width]")
    else:
        image_path = sys.argv[1]
        new_width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        main(image_path, new_width)
