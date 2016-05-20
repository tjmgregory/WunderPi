# WunderPi
A Raspberry Pi + Wunderlist e-ink desktop to-do list

With the combination of a raspberry pi and a PaPiRus display, this app will allow you to create a to do list that can sit on your desk/bedside table which will always display all the To-Dos that you have yet to complete. Saves you getting distracted by your phone when picking it up to check your To-Dos.

## Installation
*Note: Only tested on Raspberry Pi Model B, Gen. 1*

1. Get yourself a Raspberry Pi and a PaPiRus display.
2. Follow the PaPiRus software installation instructions at: https://github.com/PiSupply/PaPiRus
3. Install wunderpy2 by following the instructions here: https://pypi.python.org/pypi/wunderpy2/0.1.4
4. *Optional:* Change raspi-config
  1. Open terminal and type `sudo raspi-config`
  2. Select boot options.
  3. Choose B2 Console Autologin
5. Get to-do-ing!

### PaPiRus bugs I've come across.

#### Restarting the pi stops all functions working.

  *Solution*
  
  Add the following to your .bashrc:
  
  ```sudo service epd-fuse start```
  
#### PapirusImage using image.write('blah.jpg')
  
  ```NameError: global name 'epd' is not defined```
  
  *Solution*
  
    1. Head to `/usr/local/lib/python2.7/dist-packages/papirus`
    2. `sudo nano image.py`
    3. Add `from epd import EPD` to the list of import.
    4. And add `epd = EPD()` within the write() funtion.


## Resources
* Raspberry Pi - https://raspberrypi.org
* PaPiRus - http://papirus.ws
* Wunderlist - https://wunderlist.com
