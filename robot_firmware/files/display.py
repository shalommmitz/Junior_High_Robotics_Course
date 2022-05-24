import ssd1306
from machine import I2C, Pin

class Display(object):
    def __init__(self):
       i2c = I2C(sda=Pin(4), scl=Pin(5))
       self.display = ssd1306.SSD1306_I2C(64, 48, i2c)

    def clear(self):
        self.display.fill(0)
        self.display.show()

    def text(self, x, y, t):
        self.display.text(t,x,y)
        self.display.show()

    def hexImage(self, fn):
        f = open(fn)
        pic = f.read().split()
        f.close()

        for y in range(48):
            line = pic[y].strip()
            pixels = bin( int(line,16) )[2:]
            start = 64-len(pixels)
            for x in range( len(pixels) ):
                if pixels[x]=="1":
                    self.display.pixel(x+start, y, 1)
        self.display.show()

