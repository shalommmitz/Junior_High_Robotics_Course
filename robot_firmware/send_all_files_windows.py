import glob, os

fileNames  = glob.glob("initial_files\*.py")
fileNames += glob.glob("initial_files\*.hexImage")

for fn in fileNames:
    print("Burning "+ fn)
    cmd = "ampy.py --port COM4 put "+ fn
    print("  ", cmd)
    print("  ",  os.popen(cmd).read())
