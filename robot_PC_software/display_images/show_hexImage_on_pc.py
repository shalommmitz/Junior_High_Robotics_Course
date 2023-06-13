from __future__ import print_function
import sys
import os

argv = sys.argv
if len(argv)!=2:
    print("Usage: "+ argv[0] +" <filename.hexImage>")
    exit()
fn = argv[1]
if not os.path.isfile(fn):
    print("The file '"+ fn +"' does not exit - Aborting.")
    exit()
if len(fn)<10:
    print("The filename should end with '.hexImage' - Aborting.")
    exit()
if fn[-9:].lower()!=".heximage":
    print("The filename should end with '.hexImage' - Aborting.")
    exit()


f = open(fn)
pic = f.read().split()
f.close()

for y in range(48):
    line = pic[y].strip()
    lineAsPixels = bin( int(line,16) )[2:].zfill(64)
    print(lineAsPixels.replace("0", " ").replace("1", "@"))
    #for x in lineAsPixels:
    #    print(x, end=' ')
    #print()
