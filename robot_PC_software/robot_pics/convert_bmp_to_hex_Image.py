#!/usr/bin/env python
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
f = open(outFN, 'w')
for y in range(0,height):
    line = ""
    for x_byte in range(0,width, 4):
        c = 0
        for x in range(4):
            pixel = im.getpixel((x_byte+x,y))
            #print x_byte, x, y
            c = c*2
            if pixel==0:
                c += 1
                line += "X"
            else:
                line += "_" 

        f.write(hex(c)[2:])
    f.write("\n")
    print(line)
