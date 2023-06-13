#How to create an image and display it on the robot's display

## Prerequisits:

Make sure all needed software is installed on your PC, as detailed at the files "install_needed_software_linux.txt" and "install_needed_software_windows.txt"
      During the installation, enable the check-box "Add Python 3.7 to Path"

Make sure the firmware and related files are loaded into the robot-brain. 
This is needed to be done only once on a new robot-brain.
The needed procedure is detailed at the folder 'robot_firmware'
  
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

   -  Find which COM port the robot-brain is using:
      ON LINUX: the name is normally /dev/ttyUSB0 (or sometimes /dev/ttyUSB1)
      ON WINDOWS:
      Open the "Device Manager":
         - Right-click on "Computer"
         - choose "Manage"
         - Expand "LPT and COM ports"
         - Notice the existing serial ports (called "COM" and a digit)
         - Plug-in the robot brain to the PC, using USB cable
         - Notice the name the new COM port. This is normally "COM4"

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

    On Windows, use Putty: 
      - Select "serial" as the connection type
      - Open the Serial-ports parameters window: At the left-side "Category" tree, choose the bottom entry, which is "Serial"
      - Set "COM4" as the port
      - Set "115200" as the speed.
      - Choose "Flow control" to "None"

    On Linux, use minicom:
    - Disable hardware-flow-control
    - use "/dev/ttyUSB0" as the port 
    - Specify "115200" as the speed.

    When you are correctly connected to the robot, you should get the ">>>" prompt.
    You might need to press the "Reset" button

- Displaying the image
    Run the following:
   
       >>> import display_hexImage as d
       >>> d.display_image("abc.hexImage")
	   
