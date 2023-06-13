# How to connect to the robot, using WiFi:

Connect the the WiFi network created by the robot. This network is normally called "Born"
  
Operations on the robot:

  - Connect to the robot "Python prompt": `./webrepl_cli.py -p ofek 192.168.4.1`
  - Get a file from the robot: `./webrepl_cli.py -p ofek 192.168.4.1:/app/script.
  - Send the file "script.py" to the robot: `./webrepl_cli.py -p ofek script.py 192.168.4.1:/another_name.py`

Note: The script `webrepl_cli.py` is from https://github.com/micropython/webrepl
