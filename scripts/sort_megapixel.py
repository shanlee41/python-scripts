# Sorts pictures based on megapixel count and copies them to a separate directory

# number of megapixels
megapixels = 12
# Source directory
directory = 'D:\\Pictures'
# Destination directory
destination = 'D:\\Sorted Pictures'

import os
from PIL import Image
from shutil import copyfile

extensions = {'jpg', 'jpeg', 'png', 'tiff', 'tif', 'gif'}

directorylist = directory.split('\\')
destinationlist = destination.split('\\')

for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        extension = file.split('.')[-1]
        if extension.casefold() in extensions:
            filepath = dirpath + '\\' + file
            im = Image.open(filepath)
            megapixel = im.size[0]*im.size[1]/1000000
            if megapixel > megapixels: # Comparison logic
                pass
                pathlist = filepath.split('\\')
                dstlist = destinationlist + pathlist[len(directorylist)::]
                dstpath = ''
                for x in dstlist[0:-1]:
                    dstpath = dstpath + x + '\\'
                if not os.path.isdir(dstpath):
                    os.makedirs(dstpath)
                dstpath = ''
                for x in dstlist:
                    dstpath = dstpath + x + '\\'
                copyfile(filepath, dstpath[0:-1])