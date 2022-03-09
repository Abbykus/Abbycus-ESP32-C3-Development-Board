MicroPython ON THE ESP8266
The QDEV-ESP8266 is capable of running the MicroPython interpreted language. MicroPython is an compact Python interpretor that can run on embedded platforms. Using the familiar Python programming language you can talk to hardware and control it, much like controlling hardware with an Arduino or other embedded board. The QDEV ESP8266 board makes it easy to get started using MicroPython. Thanks to recent contributions to MicroPython you can turn an ESP8266 into a MicroPython device.

Please read MicroPython language and implementation for more information.

INSTALL MICROPYTHON
To install MicroPython firmware on the QDEV ESP8266 board see Quick reference for the ESP8266.

Also see MicroPython for the ESP8266 for the latest firmware release.

Once you have installed MicroPython on the QDEV ESP8266 board you can connect to the board via the Serial monitor in your development environment or a serial terminal emulator such as screen for Linux. You should expect to see a '>>>' prompt indicating the interactive mode where you can enter MicroPython commands or entire scripts manually.

INSTALL AMPY
In order to develop scripts for the QDEV ESP8266 module, you should install the AdaFruit MicroPython Tool ampy on your host PC which is a utility to interact with a MicroPython board (QDEV ESP8266) through the serial connection.

Ampy is a simple command line tool to manipulate files and run code on a MicroPython board. With ampy you can send files from your computer to the board's file system, download files from a board to your computer, and even send a Python script to a board to be executed.

Visit AdaFruit Ampy for instructions on installation and use of ampy.

RUN A PYTHON SCRIPT
Using the above utility Ampy you can execute python scripts from the host PC. A very simple script to blink the on-board LED can be run as follows:

Copy the main.py and blink.py files to a folder on the host PC.
Open a terminal on the host PC and navigate to the above folder.
Type one of the following (depending on your OS):
ampy --port /dev/ttyUSB0 run blink.py Linux or MacOS

ampy --port COM5 run blink.py Windows

Now you should see the ESP-12F LED blink once per second for 30 seconds.

AUTO-RUN PYTHON SCRIPTS
Python scripts can be automatically executed after Micropython boots. MicroPython executes two files after booting:

boot.py This file contains setup information and normally does not need modification.
main.py If this file exists it will be executed after boot.py.
Use Ampy to transfer main.py to the MicroPython board:

ampy --port /dev/ttyUSB0 put main.py Linux / MacOS

ampy --port COM5 put main.py Windows

To confirm that the file has been saved to the MicroPython board type:

ampy --port /dev/ttyUSB0 ls Linux / MacOS

ampy --port COM5 ls Windows

Now when the board is powered up or reset the LED will blink once per second for 30 seconds.

You can remove the main.py by typing:

ampy --port /dev/ttyUSB0 rm main.py
