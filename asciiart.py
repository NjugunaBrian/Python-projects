from PIL import Image

print('Successfully loaded image')

def read_pixels_to_array(filepath):

    image = Image.open(filepath)

    height, width = image.size

    mode = image.mode

    pixels = [[None] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            pixels[y][x] = pixel_value

    return pixels        
 
filepath = 'ascii-pineapple.jpg'
print_array = read_pixels_to_array(filepath)

print(print_array)