import PIL
from PIL import Image

def compressImage(userPreferredQuality):
    baseHeight = 300
    baseWidth = 300
    img = Image.open('imageCompressor/upload/1.jpg', 'r')
    img.resize((baseHeight, baseWidth), PIL.Image.ANTIALIAS)
    img.save('imageCompressor/upload/resized-image.jpg', quality=int(userPreferredQuality))
