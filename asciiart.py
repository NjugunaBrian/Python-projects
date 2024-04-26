from PIL import Image

image = Image.open('ascii-pineapple.jpg')
print('Successfully loaded image')
print("Image Size:", image.height, 'X', image.width)