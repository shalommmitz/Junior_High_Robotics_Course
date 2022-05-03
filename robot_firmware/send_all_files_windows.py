import glob, os

# To install ampy:   "pip install adafruit-ampy"

fileNames  = glob.glob("initial_files\*.py")
fileNames += glob.glob("initial_files\*.hexImage")

for fn in fileNames:
    print("Burning "+ fn)
    print (os.popen("ampy -p COM4 put "+ fn).read())
