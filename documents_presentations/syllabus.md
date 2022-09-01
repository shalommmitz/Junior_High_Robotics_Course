# Syllabus

## Background

This course evolved during the 11 years I have been teaching at the Ofek school for gifted children, in Jerusalem Israel.

It is composed of two courses: Basic course and Advanced course.
Both courses are for a full academic year, once weekly, each session is two academic hours.
In a typical year, this means 26 sessions.

The kids are mostly 7th or 8th grades.

## Curriculum Highlights for basic course

1. Basic theory and practice of electronics
   In parallel: build a small kit: mainly to put the theory in context and to practice soldering
2. Design the PCB for the remote control
3. Start building the robot
4. Build the remote control
5. Finish building the robot
6. Test/troubleshoot
7. If time allows: Study a bit of Python and program the robot

## Curriculum Highlights for the advanced course

1. Review/study Python
2. Make sure robot work, fix as needed
3. Lake: a fun exercise to develop Python skills
4. Basic machine vision
5. Controlling the robot using Python
6. Tie everything together: Use machine vision to control the robot
7. As time allows: basic neural network in Python


## Detailed Basic Course Syllabus

Note: The numbers are the week

 1. Teach: Electricity basic theory: 
    - Ohm law, resistors, basic circuit calculations
    - Review: electrical charge, current, voltage (charge=current*time)
    - Fun optional project: take bottles, fill w/water, simulate resistance

        - Prepare corks w/one, two or three holes
        - Mark 3 levels on the bottles
        - Ask kids to measure water drip out of the bottles (into one-time cups) on each cork/water level permutation
        - Ask them to draw the relationship and deduct Ohm's law

  2. Teach: Electronics hands-on basics: 

        - Use of multi-meter
        - Soldering: How-to + Review safety points: danger of fire, damage to eyes, burns, mark tables
        - Identifying components

     Hands-on:

        - Solder wire (each 5 cm or so) into shapes, such as rectangular or triangle

  3-5. Hands-on: First build project: Various kits
       Present to the kids examples of electronic-schematics
       Some effort to debug the kits - not insist on all kits working

  6-8. Teach:

       - Basics of Radio-frequency: what is RF, Uses to send data, modulation, Antenna
       - PCB: Alternatives (wires, wire-wrap), what it is, one side/two sides/multiple layers
       - Remote control basic-principles and schematics
       - Show installation and basic usage of DipTrace sw

       Hands-on:
       - Draw schematics for the remote using diptrace
       - design PCB for RF remote using diptrace

  10. Teach:

      - Presentation: the robot components
      - Integrated Circuits: Tube to Transistor to IC. Examples uses + packages

      Hands-on: build robot chassis, tests w/just motors and batteries

  11. Teach: Robot schematics
      Hands-on: continue build chassis
  12-15. Hands-on: Build Robot main board
  16. Hands-on: Debug robot
  17-18. Build remote control (dependant on PCB arriving)


  If time allows:

    - Fun: robot competitions, using the remotes
    - Control the robot from phone or PC using WiFi
    - Customize the picture displayed by the robot-display

A Real Basic Course (partial Corona - atypical):

 - Lesson #1 (12Oct2021): Basic soldering
 - Lesson #2 (19Oct2021): ?
 - Lesson #3 (16Nov2021): Assembling robots
 - Lesson #4 (23Nov2021): Assembling robots
 - Lesson #5 (07Dec2021): Finishing of robot chassis assembly + into to designing the remote PCB
 - Lesson #6 (14Dec2021): Remote PCB intro and start design
 - Lesson #7 (21Dec2021): Continue remote-control PCB design
 - Lesson #8 (28Dec2021): Continue design the remote PCB
 - Lesson #9 (04Jan2022): Finish remote PCB design and introduce robot schematic
 - Lesson #10 (11Jan2021): Finish previous tasks + explain robot schematics + start build rob
 - Lesson #11 (18Jan2021): Review robot schematics, tube-->transistor-->IC, cont build robot elect
 - Lesson #12 (01Feb2021): Review robot schematics + assemble robot pcb
 - Lesson #13 (08Feb2021): Hands-on intro to Python (vars, for, if)
 - Lesson #14 (22Feb2021): Build the remote control
 - Lesson #15 (22Mar2021): Continue assembling the remote control PCB
 - Lesson #16 (29Mar2021): Continue remote-control assembly
 - Lesson #17 (05Apr2021): Remote: assemble PCB + test + burn uPs
 - Lesson #18 (26Apr2021): Continue remote-assembly: continue burn chips
 - Lesson #19 (03May2021): Burn firmware to robot
 - Lesson #20 (10May2021): Burn sw to the robot brain



## Advanced Course (Work in Progress):

   1-3. Study Python:
        Either frontal intro w/exercises OR self study at CodeAcademy

   4. Teach: intro to network protocols, bits, bytes, hex. The robot protocol

      Exercise: Divide class to groups and challenge them to decode and parse messages:
          The messages will contain specs for food to server at restaurant
          One group will create the messages and the other group will draw the 'plates'
          
          Decrypt the "lake" protocol ???
          
   5. Personal project

