#Stepbot
A simple, printable, "turtle-style" robot platform designed to be inexpensive and easy to make.

This project is a work-in-progress, all designs, circuits, software and parts are far from release-ready.

## Materials

 * 3D printed parts
 * 2 28BYJ-48 stepper motors & controller boards (I got 5 off ebay for about $10)
 * 2 tyres (those "awareness" wristbands are probably the easiest thing to find)
 * Raspberry Pi 2 (or higher)
 * Raspberry Pi Camera Module (optional)
 * Rechargable USB battery (like the ones you use to charge a phone)

## Installation 

On top of base Rasbpian install:

    sudo apt-get install -y python python-pip python-dev

    sudo pip install rpi.gpio

Use `git` to pull down this repository or, perhaps better pull the repository down on another computer and copy the `software` directory over to the Raspberry Pi (unless you need the 3D models on the Pi for some reason).

## Test

Once the software is installed you can use the `commandlooper.py` script to test out the robot's hardware.

    sudo python commandlooper.py

The script will walk you through providing a few instructions for the robot which it will then loop through infinately.  If the hardware is setup correctly, the robot should be moving about now.  When this test is complete, use `ctrl-c` to stop the script and run 

    sudo python cleanup.py

to reset the GPIO pins to a known state.

## runmyrobot.com

There's a few more steps to getting Stepbot to work with runmyrobot.com.

First, if you have a camera, you might need this to get it to show up as a device:

    sudo modprobe bcm2835-v4l2

Next, you'll need python socketIO support:

    sudo pip install -U socketIO-client
