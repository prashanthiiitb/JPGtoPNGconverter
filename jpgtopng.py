#execute this from command prompt as : python programname.py sourcefolderpath destinationfolderpath
import sys
import os
from PIL import Image
#take source and destination folders as arguments
source = sys.argv[1]
dest = sys.argv[2]
#if destination folder doesn't exist, create one
if not os.path.exists(dest):
    os.makedirs(dest)
#iterate through all the given source folder images 
for image in os.listdir(source):
    jpgimg = Image.open(f'{source}\{image}')
    splitname = os.path.splitext(image)[0]
#convert each jpg image to png and save in destination folder
    jpgimg.save(f'{dest}\{splitname}.png','png')
