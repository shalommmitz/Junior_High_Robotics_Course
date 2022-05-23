import os
try:
    import uhashlib as hashlib, ubinascii as binascii
except:
    import hashlib, binascii

files = { }
files["main.py"] = b'eaed3bab714cd392de4728e3c0a48d3679c3bdbe'
files["robot.py"] = b'abc4a8e689cddf6c503566502cb0ec3ee5ab4e1c'
files["ssd1306.py"] = b'78e5a414d24986165752b3ebc8504fcfb899a1dd'
files["softuart.py"] = b'2b0534b21d343bcc21c6b9b22cbeb061c2dfd856'
files["display.py"] = b'8105ae642d0420615354e9456c8d6d5049630999'
files["webrepl_cfg.py"] = b'8b49b79b320b6436de7a08c4f4012531105a373d'
files["rf.py"] = b'75a058eb62714fa42df1457d7574f4bb3115e4a6'
files["boot.py"] = b'd890a59329e44013b4aa0636b3e1096a6eab9433'
files["demo.py"] = b'5462e508620dda37ca5555ad57f90a61b1c2ae4d'
files["init_robot.py"] = b'f854d0e362c550257ca8a944e2a9b8c7429d06d5'

existingFiles = os.listdir()
for fn in files.keys():
    if not fn in existingFiles:
        print( "File", fn, " does not exist." )
        continue
    f = open(fn)
    fileAsStr = f.read().encode("utf-8")
    f.close()
    f = open(fn); fileAsStr = f.read().encode("utf-8"); f.close()
    hash = binascii.hexlify( hashlib.sha1(fileAsStr).digest() )
    if hash != files[fn]:
        print( "File", fn, " has the wrong checksum." )
        print(      "actual hash:", hash)
