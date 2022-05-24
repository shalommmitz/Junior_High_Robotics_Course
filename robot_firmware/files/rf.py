import softuart, ubinascii

MESSSAGE_LENGHT = 5
# Message Format:
# Header: five bytes of 0xAA
# first  byte: 7 (MSB): parity  
#              6-4    : reseved to zeron (to diff from header)
#              3-0    : robotId
# second byte: 7 (MSB): parity
#              6      : command parity 
#              5      : left wheel direction: 1=forward 0=backward
#              4      : right wheel direction: 1=forward 0=backward
#              3      : LED state
#              2-0    : command: 0 blink ID, 1 move + LED state 
# third byte:  7 (MSB): parity
#              6-0    : left wheel time 
# forth  byte: 7 (MSB): parity
#              6-0    : right wheel time 
# fifth  byte: XOR of all prev bytes

SYNC = 0xAA
u = softuart.SoftUart(13)

class RF(object):
    def __init__(self):
        self.MSG_LEN = 5
    def getPacket(self):      
        # msg states: 0: outside, 1: in hdr, 2: in msg
        msg = bytearray()
        state = 0
        prevRxByte = 0x00
        for i in range(1000):
            rxByte = u.getSingleChar()
            if prevRxByte == SYNC and rxByte == SYNC:
                msg = u.getCharsUntilTimeOutOrSpecifiedNum(8)
                break
            prevRxByte = rxByte

        if len(msg)<self.MSG_LEN: 
            print( "msg too short:"+ str(ubinascii.hexlify(msg)) )
            return msg

        numSync = 0
        if msg[0]==SYNC: numSync = 1
        if msg[1]==SYNC: numSync = 2
        if msg[2]==SYNC: numSync = 3
        msg = msg[numSync:numSync+5]

        print( "msg before fixing: "+ str(ubinascii.hexlify(msg)) )
        msg = self.verifyFixRejectMsg(msg)
        if msg:
            print( "msg after fixing: "+ str(ubinascii.hexlify(msg)) )
        return msg

    def verifyFixRejectMsg(self, msg):
        def getNumBitsInByte(b):
            numBitsOne  = 0
            mask = 1
            for i in range(8):
                if mask & b:
                    numBitsOne = numBitsOne+1
                mask = mask << 1
            return numBitsOne

        def getIndexBitsOnXor(b):
            ix  = 0
            mask = 1
            for i in range(8):
                if mask & b:
                    ix = i
                mask = mask << 1
            return ix
        def getParity(b):
            numBitsOne  = 0
            mask = 1
            for i in range(8):
                if mask & b:
                    numBitsOne = numBitsOne+1
                mask = mask * 2
            parity = numBitsOne % 2
            return parity

        xor = 0
        for b in msg:
            xor ^= b
        numBitsInXor = getNumBitsInByte(xor)
        indexBitOnXor = getIndexBitsOnXor(xor)

        numParityErrors = 0; IndexOfByteParityError = None
        for i in range(len(msg)):
            c = msg[i]
            if getParity(c):
                numParityErrors += 1
                IndexOfByteParityError = i
        if numParityErrors==0 and numBitsInXor==0:
            print("msg perfect")
            return msg 
        if numParityErrors==1 and numBitsInXor==1:
            fixedMsg = bytearray()
            for i in range(len(msg)):
                if i==IndexOfByteParityError:
                    fixedMsg.append( msg[i] ^ xor )
                else:
                    fixedMsg.append( msg[i] )
            print("msg fixed")
            return fixedMsg
        print("msg rejected: too many parity errors")
        return None

    def interpetMsg(self, msg):
        if len(msg)!=5:
            msgDict = { "Error": "Incorrect Lenght" }
            return msgDict
        msgDict = { "Error": None }
        
        commandValue = msg[1] & 0b00000111
        if commandValue==0:
            command = "OCR_BLINK_ID"
        elif commandValue==1:       
            command = "OCR_MOVE_SET_LED"
        else:
            msgDict = { "Error": "Unknown command ("+ hex(commandValue) +")" }
            return msgDict
    
        commandParity = bool(msg[1] & 0b01000000)
        
        ledState = bool(msg[1] & 0b00001000)

        rightMotorDirctionValue = bool(msg[1] & 0b00010000)
        if rightMotorDirctionValue:
            rightMotorDirction = "FORWARD"
        else:
            rightMotorDirction = "BACK"
 
        leftMotorDirctionValue = bool(msg[1] & 0b00100000)
        if leftMotorDirctionValue:
            leftMotorDirction = "FORWARD"
        else:
            leftMotorDirction = "BACK"

        leftMotorDuration = int(msg[2] & 0b01111111)

        rightMotorDuration = int(msg[3] & 0b01111111)
        remoteId = int(msg[0] & 0b00001111)
        print("remoteId:"+ str(remoteId) )

        msgDict = { "command": command,"commandParity": commandParity,"ledState": ledState }
        msgDict["rightMotorDirction"] = rightMotorDirction
        msgDict["leftMotorDirction"] = leftMotorDirction
        msgDict["rightMotorDuration"] = rightMotorDuration
        msgDict["leftMotorDuration"] = leftMotorDuration
        msgDict["remoteId"] = remoteId
        return msgDict

    def executePacket(self, msg):
        print( "Executing:"+ str(ubinascii.hexlify(msg)) )
        msgDict = self.interpetMsg( msg)
        print ("Executing:")
        for k in msgDict.keys():
            print(k, msgDict[k])      
        return
