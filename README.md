<p align="center">
  <h3 align="center">Junior High Robotics Course</h3>

  <p align="center">
    An open-source and open-hardware course, designed to make Technology cool.
  </p>
</p>
<br>

This repository holds the materials of a robotics course that was given for more than 10 years to gifted students. The course teaches the basics of electronics, programming and robotics. The course aims to make students 'at home' with advanced, deep technologies, in hope that more of them will choose STEM as careers.
During the course, the students build a robot, which is affordable enough so they can take it home at the end of the year. This is a great motivator.

![Alt text](robot_and_remote.png?raw=true "The robot and remote-control assembled")

## Table of contents

- [Course Overview](#course-overview)
- [Content of Subdirectories](#content-of-subdirectories)
- [Prerequisites and Installing](#prerequisites-and-installing)
- [Author](#author)
- [License](#license)

## Course Overview

The course was given multiple years to 7Th, 8Th and 9Th graders at the i[Ofek Gifted school](http://projects.jerusalemfoundation.org/education/education/ofek-school-for-gifted-children.aspx), located at Jerusalem, Israel.
This course teaches the following

- The basic principles of electricity (Ohm's law and related terms)
- The basic principles of electronics, including use of multi-meter
- Reading electronics schematics
- Design of PCBs
- Soldering and trouble-shooting electronic circuits
- Basic Python skills


## Content of Subdirectories

- documents_presentations:
    - [The course syllabus](documents_presentations/syllabus.md)
    - [The list of parts used in the course, including links for each item in Ali-Express](documents_presentations/22_08_Ofek_robotics_purchases.xlsx)
    - [Presentation: Motivation for the course (Hebrew)](documents_presentations/advocating_technology_at_junior_high_Hebrew.pptx)
    - [Presentation: Overview of Electronics (Hebrew)](documents_presentations/electronics_overview_Hebrew.ppt)
    - [Hands-on fun way to illustrate voltage/current/resistance and their relationship (Hebrew)](documents_presentations/ohm_law_experiment.doc)
    -[Presentation: Overview of the robot (Hebrew)](documents_presentations/robot_overview_Hebrew.ppt) 

- remoteControl_firmware
- remoteControl_hardware
- robot_firmware
- robot_hardware
- robot_PC_software

## So, you want to teach this course ?

Here is what you will need:

- One time: One item of: PIC programmer, [PIC basic pro compiler](http://store.melabs.com/prod/PBP/PBP3-2.html)
- One time: For each student: A PC or laptop,working bench, a soldering iron
- One time: For every 5 students: a multimeter, a magnifing glass, pliers, cutter 
- Every year: [kits, robots and remote parts](documents_presentations/22_08_Ofek_robotics_purchases.xlsx)


## Author

**Shalom Mitz** - [shalommmitz](https://github.com/shalommmitz)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE ) file for details.

## Apendix A: Parts List
| Quantity per student       | Quantity Ordered | Description                 | Order | Del | Price USD | Used by      | URL                                                                                                                                                                                   |                                 |
|----------------------------|------------------|-----------------------------|-------|-----|-----------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
|                            |                  |                             |       |     |           |              |                                                                                                                                                                                       |                                 |
| First Project (Kit)        |                  | Kits                        |       |     |           |              |                                                                                                                                                                                       |                                 |
| 4                          | 5                | Hour-glass leds kit         | 24Aug |     | 17.71     | Initial kit  | https://www.aliexpress.com/item/1005002305819829.html                                                                                                                                 |                                 |
| 4                          | 5                | Alarm clock kit             | 24Aug |     | 26.59     | Initial kit  | https://www.aliexpress.com/item/4000302775578.html                                                                                                                                    |                                 |
| 4                          | 5                | Metal detector              | 24Aug |     | 9.14      | Initial kit  | https://www.aliexpress.com/item/33004705384.html                                                                                                                                      |                                 |
| Parts for robot and remote |                  |                             |       |     |           |              |                                                                                                                                                                                       |                                 |
| 15                         | 8                | Wheel Chassis               | 01Sep |     | 68.92     | robot        | https://www.aliexpress.com/item/1005004589986093.html                                                                                                                                 |                                 |
| 0                          | 7                | Wheel Chassis               | 04Sep |     | 60.34     | robot        | https://www.aliexpress.com/item/1005004589986093.html                                                                                                                                 |                                 |
| 1                          | 0                | 25 PCB version 1.7          | 03Sep |     | 27.51     | robot        | https://jlcpcb.com/                                                                                                                                                                   |                                 |
| 1                          |                  | PCBs for Remote             |       |     |           | remote       | https://jlcpcb.com/                                                                                                                                                                   |                                 |
| 2                          | 2                | 10 uP PIC12F675 I/P         | 04Sep |     | 26.7      | remote       | https://www.aliexpress.com/item/4000052205464.html                                                                                                                                    |                                 |
| 1                          | 0                | 1000 LED                    |       |     |           | robot        | https://www.aliexpress.com/item/Free-shipping-1000PCS-5-value-5mm-diffused-red-yellow-blue-green-white-R-G-B-W/2048531042.html                                                        |                                 |
| 1                          |                  | 100 x 40-pin stright Female |       |     |           | robot        | http://www.aliexpress.com/item/100PCS-2-54mm-40-Pin-Stright-Female-Single-Row-Pin-Header-Strip-PCB-Connector/32596334536.html                                                         |                                 |
| 3                          | 3                | 10 L239D DIP IC             | 04Sep |     | 7.1       | robot        | https://www.aliexpress.com/item/32844099228.html                                                                                                                                      |                                 |
| 1                          | 3                | 10 14pin DIP socket         | 04Sep |     | 7.02      | robot        | https://www.aliexpress.com/item/32799921132.html                                                                                                                                      |                                 |
| 2                          | 3                | 10 16pin socket             | 04Sep |     | 6.42      | robot        | https://www.aliexpress.com/item/32800892159.html                                                                                                                                      |                                 |
| 15                         | 15               | Wemos D1 Mini V3.0.0        | 05Sep |     | 32.55     | robot        | https://www.aliexpress.com/item/1005001621896145.html                                                                                                                                 |                                 |
| 12                         | 15               | Oled Display 64x48          | 05Sep |     | 27.75     | robot        | https://www.aliexpress.com/item/1005001621659840.htmlhttps://www.aliexpress.co/item/Free-Shipping-0-66-inch-Wemos-Oled-64X48-IIC-I2C-LCD-OLED-LED-Dispaly-Shield-for/32807210516.html |                                 |
| 2                          | 2                | 20 8pin socket              | 05Sep |     | 4.02      | remote       | https://www.aliexpress.com/item/32878848553.html                                                                                                                                      |                                 |
| 0                          | 0                | 100 x 1000u cap             |       |     |           | remote+robot | http://www.aliexpress.com/item/Free-Shipping-DIP-Electrolytic-capacitor-1000UF-16V-8-12mm-100pcs-lot-NEW-in-stock-if-can/2010462041.html                                              |                                 |
| 5                          | 0                | 500pcs 220 ohm resistors    |       |     | 8.37      | remote+robot | https://www.aliexpress.com/item/32829082640.html                                                                                                                                      | Note: 5 per robot, 1 per remote |
| 2                          | 0                | 200pcs 100K ohm             |       |     | 3.31      | robot        | https://www.aliexpress.com/item/1005002000626397.html                                                                                                                                 | Note: 2 per robot               |
| 12                         | 25               | RF TX RX + ANT              | 05Sep |     | 21.29     | remote+robot | https://www.aliexpress.com/item/32980820915.html                                                                                                                                      |                                 |
| 3                          | 7                | 25pcs push btn              | 05Sep |     | 7.25      | for remote   | https://www.aliexpress.com/item/32834276752.html                                                                                                                                      |                                 |
| 0                          | 0                | 10 2 AA Battery Holder      |       |     | 6.99      | for remote   | http://www.aliexpress.com/item/10PCS-2-AA-3A-Battery-3V-Holder-Box-Case-with-5-5-Leads-and-ON-OFF/1985883563.html                                                                     |                                 |
| 1                          | 2                | 20 pcs SN74HC04N IC         | 05Sep |     | 8.06      | for remote   | https://www.aliexpress.com/item/1005002920656915.html                                                                                                                                 |                                 |
| 4                          | 13               | 10 pcs terminal block       | 05Sep |     | 24.12     | remote+robot | https://www.aliexpress.com/item/4000899450689.html                                                                                                                                    |                                 |
| 12                         | 7                | power bank                  | 05Sep |     | 63.7      | for robot    | https://www.aliexpress.com/item/1005004701731413.html                                                                                                                                 |                                 |
|                            | 7                | power bank                  |       |     | 63.7      | for robot    | https://www.aliexpress.com/item/1005004701731413.html                                                                                                                                 |                                 |
| 12                         | 6                | USB power cable             | 05Sep |     | 4.32      | robot        | https://www.aliexpress.com/item/4001022946203.html                                                                                                                                    |                                 |
|                            | 6                | USB power cable             |       |     | 5.32      |              | https://www.aliexpress.com/item/4001022946203.html                                                                                                                                    |                                 |
|                            | 6                | USB power cable             |       |     | 6.32      |              | https://www.aliexpress.com/item/4001022946203.html                                                                                                                                    |                                 |
|                            |                  | TOTAL USD                   |       |     | 532.88    |              |                                                                                                                                                                                       |                                 |

