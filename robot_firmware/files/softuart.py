#  Originally from: h__ps://forum.micropython.org/viewtopic.php?t=2765
import time
import machine

class SoftUart(object):
    #1190 works better than 1200. CPU speed is unchanged from the default default (80MHz)
    def __init__(self, rx_pin_number, baud = 1200):         
        self.rx = machine.Pin(rx_pin_number)
        self.rx.init(machine.Pin.IN)
        self.baud(baud)
        self.timeout = False
    def baud(self, baud):
        self.bitdelay = 1000000 // baud - 200
    def timeout(self):
        return self.timeout
    def getSingleChar(self, timeout=20):
        t = 0
        self.timeout = False
        while self.rx():
            time.sleep_us(20)
            t = t + 1
            if t < timeout*5:
                pass
            else:
                self.timeout = True
                return -1
        time.sleep_us(self.bitdelay + self.bitdelay//8)
        dat = 0
        for i in range(8):
            dat = dat >> 1
            if self.rx():
                dat = dat | 0x80
            else:
                dat = dat | 0x00          # For consistent timing
            time.sleep_us(self.bitdelay)
        time.sleep_us(self.bitdelay//4)   # Shroten to allow for short stop-bit
        return dat
    def getCharsUntilTimeOutOrSpecifiedNum(self, num=0):
        dat=bytearray(0)
        while True:
            t = self.getSingleChar()
            if t==-1: continue
            if self.timeout:
                return dat
            else:
                dat.append(t)
            if num > 0:
                if num > 1:
                    num = num - 1
                else:
                    return dat
