import os, uhashlib as hashlib, ubinascii as binascii

files = { }
files["main.py"] = b'eaed3bab714cd392de4728e3c0a48d3679c3bdbe'
files["robot.py"] = b'02947ffb1631ecf43390ea6e02e2b98f6e966c73'
files["ssd1306.py"] = b'78e5a414d24986165752b3ebc8504fcfb899a1dd'
files["softuart.py"] = b'2b0534b21d343bcc21c6b9b22cbeb061c2dfd856'
files["display.py"] = b'924bdfdfa6d2c916b9dbdc522a367680aa71c94f'
files["webrepl_cfg.py"] = b'8b49b79b320b6436de7a08c4f4012531105a373d'
files["rf.py"] = b'8717ebe2a243fd5d26c6470e3945494ec9ac7d4d'
files["boot.py"] = b'd890a59329e44013b4aa0636b3e1096a6eab9433'
files["demo.py"] = b'ec32769f8adcea90fb075148540ba0808efeb286'

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