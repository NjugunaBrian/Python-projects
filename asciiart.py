from PIL import Image

ASCII_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def read_pixels_to_array(filepath):

    image = Image.open(filepath)

    height, width = image.size

    pixels = list(image.getdata())

    pixel_array = [pixels[i * width: (i + 1) * width] for i in range(height)]

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

def convert_to_ascii(intensity_matrix, ascii_characters):

    ascii_matrix = []
    for row in intensity_matrix:
        ascii_row = []
        for p in row:
            index = ascii_characters[int(p/255 * len(ascii_characters)) - 1]
            ascii_row.append(index)
        ascii_matrix.append(ascii_row)    

    return ascii_matrix



print("Successfully constructed ASCII matrix!")



filepath = 'ascii-pineapple.jpg'
print_array = read_pixels_to_array(filepath)
print_average = read_pixels_to_brightness(print_array, algo_name='average')
#print("Iterating through pixel brightnesses:", print_average)
ascii_representation  = convert_to_ascii(print_average, ASCII_characters)
print("Iterating through pixel ASCII characters:", ascii_representation)

#I am representing 255 characters onto 70 characters of the ACII character matrix.
#For each number, I map it onto the appropriate character