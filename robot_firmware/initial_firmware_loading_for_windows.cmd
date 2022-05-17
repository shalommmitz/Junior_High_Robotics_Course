
REM Need python: you can Download and install from python.org. 

REM IMPORTANT: Turn on "Add Python to Path" at first screen of installation

REM Install the sw used to burn the 'robot brain' (=ESP8620):   pip install esptool

python -m esptool erase_flash

python -m esptool write_flash --flash_size=detect 0 firmware.bin
