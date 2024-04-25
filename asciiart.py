import Image
im = Image.open('https://robertheaton.com/images/ascii-pineapple.jpg')
print('Successfully loaded image')
print("Image Size:", im.height, 'X', im.width)