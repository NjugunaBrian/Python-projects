from PIL import Image
from colorama import Fore, Style

ASCII_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255


def read_pixels_to_array(image, height):


    image.thumbnail((height, 200))
    new_width = 50
    new_height = 50

    resized_image = image.resize((new_width, new_height))
    
    pixels = list(resized_image.getdata())

    pixel_array = [pixels[i: i+resized_image.width] for i in range(0, len(pixels), resized_image.width)]

    return pixel_array        


def read_pixels_to_brightness(pixelMatrix, algo_name="average"):
    intensity_matrix = []
    for y in range(len(pixelMatrix)):
        intensity_row = []
        for x in range(len(pixelMatrix[y])):
            R = pixelMatrix[y][x][0]
            G = pixelMatrix[y][x][1]
            B = pixelMatrix[y][x][2]

            if algo_name == 'average':
                intensity = (R + G + B) / 3
            elif algo_name == 'max_min':
                intensity = (max(pixelMatrix) + min(pixelMatrix) / 2)

            elif algo_name == 'luminosity':
                intensity = 0.21*R + 0.72*G + 0.07*B
            else:
                raise Exception ("Unrecognized algo_name: %s" % algo_name)        

            
            intensity_row.append(intensity)

        intensity_matrix.append(intensity_row)

    return intensity_matrix            

def normalize_intensity_matrix(intensity_matrix):
    normalized_intensity_matrix = []
    flattened_matrix = [value for row in intensity_matrix for value in row]
    max_pixel = max(flattened_matrix)
    min_pixel = min(flattened_matrix)
    for row in intensity_matrix:
        rescaled_row = []
        for p in row:
            r = MAX_PIXEL_VALUE * (p - min_pixel) / float(max_pixel - min_pixel)
            rescaled_row.append(r)
        normalized_intensity_matrix.append(rescaled_row) 

    return normalized_intensity_matrix 


def convert_to_ascii(intensity_matrix, ascii_characters):

    ascii_matrix = []
    for row in intensity_matrix:
        ascii_row = []
        for p in row:
            index = ascii_characters[int(p/255 * len(ascii_characters)) - 1]
            ascii_row.append(index)
        ascii_matrix.append(ascii_row)    

    return ascii_matrix

def print_ascii_martix(ascii_matrix, text_color):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        print(text_color + "".join(line))

    print(Style.RESET_ALL)



filepath = 'ascii-pineapple.jpg'
image = Image.open(filepath)

print_array = read_pixels_to_array(image, 1000)
print_average = read_pixels_to_brightness(print_array, algo_name='average')
#print("Iterating through pixel brightnesses:", print_average)
normalized_matrix = normalize_intensity_matrix(print_average)
ascii_representation  = convert_to_ascii(normalized_matrix, ASCII_characters)
#print("Iterating through pixel ASCII characters:", ascii_representation)
print_ascii_martix(ascii_representation, Fore.GREEN)

#I am representing 255 characters onto 70 characters of the ACII character matrix.
#For each number, I map it onto the appropriate character