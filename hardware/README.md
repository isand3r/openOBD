### openOBD Hardware

The files in this folder are all contained in an Altium project. To view the files, you will need either Altium Designer or other compatible software (newer versions of [Eagle](http://www.autodesk.com/products/eagle/overview) can import Altium projects).

#### Circuit Schematics (Images) (coming soon)

#### B.O.M. (coming soon)

#### Programming the on board microcontroller

The on board microcontroller (ATtiny25) is wired to sense the vehicles battery voltage using its ADC. It can in turn controll a switch that can short the RUN pins on the Raspberry Pi Zero and wake/reboot it. The Raspberry Pi can communicate with the microcontroller through SPI interface in order to retreive data and/or reprogram it. This setup provides the user flexibility in implementing a custom power management. Following the instructions below, the ATtiny can be easily programmed:

* Compile your program using your favourite IDE/compiler ([Arduino IDE](http://www.arduino.org/downloads) or [Atmel studio](http://www.microchip.com/development-tools/atmel-studio-7) are options)
* Locate the generated .hex file and transfer it to the Raspberry Pi ([winSCP](https://winscp.net/eng/download.php) is a good tool)
* On the pi run 'sudo apt-get install avrdude' 
* [Configure](www.google,ca) avrdude using the following settings
1. 
    * id=pi0;
    * desc  = "Use the Linux sysfs interface to bitbang GPIO lines";
    * type = "linuxgpio";
    * reset = 18;
    * sck = 21;
    * mosi = 20;
    * miso = 19;

#### PCB Manufacturer

For our PCB, we used [pcbway.com](https://www.pcbway.com/). They are cheap, fast, and reliable. (images coming soon)
