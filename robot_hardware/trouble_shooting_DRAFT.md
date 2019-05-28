My robot does not move
----------------------
Those are the possible causes:

1. No power
2. 'Brain' not fully functional
3. Motors not connected
4. Issue with the H-Bridge IC (U2, L293D)

Procedure to Fix:

1. Verify that power is Ok
   The center LED should be on. If not, you have no power.
   If the LED is on, use multimeter (at V-DC-20V position) to measuer the input voltage. It should be atleast 4.8V. If less, you probably have to change the battries.
   If there is no voltage, start measuring voltage from the battries, until you find where is the disconnect.

2. Verify brain works Ok
   We proceed to this state assuming we verified that power is Ok.
   The easiest way to verify that the brain is fully functional is to switch termorarirly to brain from a known-to-be-working robot. If another, known-to-work, brain is not available, the best way is to continue the procedure, while watching carfully the performance of the brain. Another possiblity is to reflash the brain (rarly needed) and reload all the files.

NEED TO ADD LINK TO FLASHING THE FILES

3.  Verify that the motors are connected
   This one is easy: Using your hand, turn one wheel both ways. One of the two LEDs associated with each whell should light momentarily. Repeate for the other wheel. Fix any issue found.

4. Verify the correct operation of the H-bridge.  
   Issues with the H-bridge are the most common reason why robot won't move.
   Here are the steps to debug this IC:
   4.1. Open the schematics and zoom on U2. The schematic is at NEED TO ADD LINK TO SCHEMA
   4.2  Get a multimeter, and set it to measure Volts-DC-20V. Connect the "-"/black probe to one of the ground point of the robot, for example at the battries "-" terminal.
   4.3 Look at the schema. The H-bridge IC has two connections to the power-supply. Check that both of those connections are connected to the 5V or so comming from the battries.
   4.4 Verify connection from the brain to the pwmLeft and pwmRight points
       NEED TO ADD CODE
       NEED  TO ADD LINK TO PROCEDURE TO GET REPL (Python prompt).
