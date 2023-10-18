The scematics of the remote control
===========================

Intrduciotion
-------------

The remote control is an optional part of the robots, that allows controlling the robot (move and turn) using the remote's buttons.
The remote transmits the commands on the free-use 433MHz radio frequency.

During the course, each student normally designs her own PCB (Printed Circute Board) for the remote. 
However, a pre-existing PCB design is present in this directory, if needed.
The software used for the schema capture and for the PCB design is the free version of diptrace. Sorrowfully, diptrace is available only under Windows. However, it is known to run under Linux/Wine.

The rest of the document intruduces the components used and the connections between them.

Terminal
--------
Connects the two wires from the battery holder to the PCB.
    Note: Mark the + and - so you will be able to tell where to connect the black/red wires.
    Note: The battery + is called Vcc. The battery - is called Ground.

Capacitor
---------
Connects to Vcc and to Ground. Stabilizes the voltage.
    Note: Mark the + on the PCB.

Microprocessor
--------------
Runs software that sends message to the robot using the RF module.
    Find by searching for component "PIC12F675_P":wq
    Sends a message when one of the keys are pressed.
    Microprocessor leg function list:
       - Leg number 1 connects to Vcc and leg number 8 to Ground.
       - Legs number 2, 3, 5 and 6 are connected to the switches; they are inputs.
       - Leg number 7 is connected to the RF module (pin 2) AND to the LED-resistor.      
       - Leg number 4 is not used.
    Note: Since the microprocessor needs to be available for software updates, it is not soldered directly to the PCB.
          Instead, a socket is soldered to the PCB and the microprocessor is inserted into the socket.
          This does not affect the PCB or the schematic.

LED and LED-resistor
--------------------
    The LED-resistor is connected to the microprocessor (leg 7) and to the + of the LED.
    The + of the LED is connected to the LED-resistor and the - to ground.
    Note: The resistor's function is to limit the current that passes through the LED.

RF module
---------
    The RF module sends information from the microprocessor to the robot as radio waves.
    RF module leg function list:
       - Leg number 3 connects to Vcc and leg number 4 to Ground.
       - Leg number 2 is connected to the microprocessor (leg 7).
       - Leg number 1 is not used.
    Note: you have to solder an antenna to the RF module. This does not affect the PCB. 
