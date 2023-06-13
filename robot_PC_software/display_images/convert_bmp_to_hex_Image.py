#!/usr/bin/env python3
import  sys, os
from PIL import Image

argv = sys.argv
if len(argv)!=2:
    print("Usage: "+ argv[0] +" <48x64 blackwhite bmp filename>")
    exit()
fn = argv[1]
if not os.path.isfile(fn):
    print("The file '"+ fn +"' does not exit - Aborting.")
    exit()
if len(fn)<4:
    print("The filename should end with '.bmp' - Aborting.")
    exit()
if fn[-4:].lower()!=".bmp":
    print("The filename should end with '.bmp' - Aborting.")
    exit()

outFN = fn[:-4] +".hexImage"
print("Writing output to '"+ outFN +"'.")
im = Image.open(fn)
x = 0
y = 0
width, height = im.size
if width != 64:
    print("ERROR: width must be equal to 64 - Aborting.")
    exit()
if height != 48:
    print("ERROR: height must be exactly 48 - Aborting.")
    exit()

f = open(outFN, 'w')
for y in range(0,height):
    line = ""
    for x_nibble in range(0,width, 4):
        c = 0
        for x in range(4):
            pixel = im.getpixel((x_nibble+x,y))
            #print x_nibble, x, y, pixel
            c = c*2
            if pixel==0 or pixel==(0,0,0):
                c += 1
                line += "X"
            else:
                line += "_" 

        f.write(hex(c)[2:])
    f.write("\n")
    print(line)
