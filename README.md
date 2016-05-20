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

#### PaPiRus bug
You may find that after installing PaPiRus everything will work fine, however when you restart all of the commands cause errors. The solution to this is to add the following to your .bashrc: `sudo service epd-fuse start`
  
I've let them know about this bug on their repo with this solution, but this hasn't been fixed yet.


## Resources
* Raspberry Pi - https://raspberrypi.org
* PaPiRus - http://papirus.ws
* Wunderlist - https://wunderlist.com
