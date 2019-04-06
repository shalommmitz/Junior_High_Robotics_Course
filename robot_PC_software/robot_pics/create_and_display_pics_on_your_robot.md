#How to create an image and display it on the robot's display

## Prerequisits:

On Ubuntu:

- Install pillow: pip install pillow 
- Optional: install pinta: apt install pinta

On Windows:

- Install python 3.x from python.org. Enable the check-box "Add to Path"
- Install the 'pillow' module (provides 'Image') (E.g.: pip install pillow)
- Optional: Install notepad++ (to edit code files) 
- Optional: Install paint.net (to edit the .bmp image files)

## Create a new image that have the following attributes:

     size:  64 x 48   (This is the size of the display)
	 Color depth: black & white
   Or, you can start with one of the pre-existing images in this directory.
 
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
   
   Details on ampy: https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy
   
   Details on webrepl: https://github.com/micropython/webrepl

## Displaying the image on the robot:

Connect to the robot and get the REPL prompt.  
Connecting to the robot can be done:

- Using WEBREPL over WiFi
Or 
- Using any 'serial terminal' program, such as putty or minicom over USB

Use 'display_hexImage.py', which is present on your robot, to display the file.
   For example:
   
       >>> import display_hexImage as d
       >>> d.display("abc.hexImage")
	   
