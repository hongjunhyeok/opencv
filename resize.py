from PIL import Image
import os, sys

path = "img/empty_200909/9/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((450,343), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpeg', 'JPEG', quality=100)

resize()