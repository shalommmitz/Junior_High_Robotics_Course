#How to create an image and display it on the robot's display

## Prerequisits:

On Ubuntu:

- Install pillow: pip install pillow 
- Optional: install pinta: apt install pinta

On Windows:

- Install python 3.x (x86-64, 64-bit) from python.org. 
     
      During the installation, enable the check-box "Add Python 3.7 to Path"
  
- Install the 'pillow' and ampy Python modules:
-  
     pip install pillow adafruit-ampy

- Install the serial driver for the 'Wemos D1 Mini' (AKA, the robot brain).

    Can be found in the file 'ch341ser_win_3.4.zip' 
    For example at https://wiki.wemos.cc/downloads

- Install putty (used to run commands on the robot-brain)
     
- Optional: Install notepad++ (to edit code files) 
- Optional: Install paint.net (to edit the .bmp image files)

## Create a new image that have the following attributes:

     size:  64 x 48   (This is the size of the display)
	 Color depth: black & white
   Or, you can start with one of the pre-existing images (.bmp) in this directory.
 
## Edit the image

You can edit the image with any image editing tool, such as mspaint, gimp, paint.net or pinta.

## Save the image, specifing the 'bitmap' format.

   It is important to keep the correct size and color depth

## Create the .hexImage file:

   The .hexImage file can be used by the robot software.
   
   Run:
   
        python convert_bmp_to_hex_Image.py <file_name.bmp>
        
   This will create a .hexImage file

## Preview the .hexImage file:

   run: 
   
        python show_hexImage_on_pc.py <file_name.hexImage>.

   If you don't like what you see, you can edit/save/convert/preview until happy :-)

## Upload the .hexImage file to the robot:

   Loading the file might be done using ampy or webrepl

   Using ampy:   
   
       Linx:  ampy -p /dev/ttyUSB0 put <file name>
   
       Windws:  ampy -p com4 put <file name>
   
   Details on ampy: https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy
   
   Details on webrepl: https://github.com/micropython/webrepl

## Displaying the image on the robot:

Connect to the robot and get the REPL prompt.  
Connecting to the robot can be done:

- Using WiFi: 

    Download from github the repository "webrepl.
    
    The robot 'publish' a WiFi network, called 'born' by default.
    Connect to this network.

    Now, open the .html page in the 'webrepl' repository, by double-clicking on the file.
    

- OR, using a USB cable:

    Connect the robot to a PC using a standard 'Android' usb cable
    Run any 'serial terminal' program, such as putty or minicom.

    If you are using putty: select "serial" as the connection type, "COM4" as the port and "115200" as the speed.

    If you are using minicom: Disable hardware-flow-control, use "/dev/ttyUSB0" as the port and "115200" as the speed.

    When you are correctly connected to the robot, you should get the ">>>" prompt.

- Displaying the image
    Run the following:
   
       >>> import display_hexImage as d
       >>> d.display_image("abc.hexImage")
	   
