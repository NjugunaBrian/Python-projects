from PIL import Image

print('Successfully loaded image')

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
                intensity = (R + G + B) / 3.0
            elif algo_name == 'max_min':
                intensity = (max(pixelMatrix) + min(pixelMatrix) / 2.0)

            elif algo_name == 'luminosity':
                intensity = 0.21*R + 0.72*G + 0.07*B
            else:
                raise Exception ("Unrecognized algo_name: %s" % algo_name)        

            
            intensity_row.append(intensity)

        intensity_matrix.append(intensity_row)

    return intensity_matrix            



print("Successfully constructed brightness matrix!")



filepath = 'ascii-pineapple.jpg'
print_array = read_pixels_to_array(filepath)
print_average = read_pixels_to_brightness(print_array, algo_name='luminosity')
print("Iterating through pixel brightnesses:", print_average)

