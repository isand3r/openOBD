# openOBD [![Build Status](https://travis-ci.org/mulvenna/openOBD.svg?branch=master)](https://travis-ci.org/mulvenna/openOBD)
- An open-source vehicle telemetry system based on the [Raspberry Pi 0](https://www.raspberrypi.org/blog/raspberry-pi-zero) that supports OBD-2 and includes several sensors
- Originally developed as a UBC Electrical & Computer Engineering [Capstone Project](https://www.ece.ubc.ca/courses/capstones) for [Mojio](https://www.moj.io/)

![photo](https://raw.githubusercontent.com/isand3r/openOBD/master/docs/photo.jpg)

### Setup


#### 1. Set up the Raspberry Pi

Follow this guide: https://www.raspberrypi.org/documentation/installation/installing-images/

The software requires a Linux-based operating system such as Ubuntu or Raspbian.

#### 2. Attach the board

Should be straightforward - attach the board using the GPIO socket with the board hanging overtop of your rpi.

#### 3. Clone this repository
On your raspberry pi, using the command line, run `git clone https://github.com/isand3r/openOBD`.

The Command line interface to get values from the sensors can be run using the file `app.py`

#### 4. Install dependencies

See the dependencies list at the bottom.

#### 5. Set up GSM (Optional)

Data readings can be saved to a file and uploaded via wifi, or for constant connectivity, there is a GSM module included.
All info on the GSM module can be found here: https://learn.adafruit.com/adafruit-fona-808-cellular-plus-gps-breakout/downloads#datasheets-and-app-notes

## Usage

### Command Line Application
```
cd software/openobd/
python3 app.py
```

![screenshot](https://raw.githubusercontent.com/isand3r/openOBD/master/docs/screenshot.png)

### Configuration File
The configuration file `software/openobd/configuration/config.ini` (parsed using [configparser](https://docs.python.org/3/library/configparser.html)) is used to select the class that will be used for each sensor device (GPS, thermometer, etc). If mock devices are used (and if a few `import` lines are commented out in `software/openobd/app.py`), the command line application can be run on a regular PC without requiring the openOBD hardware.

### Tests
```
cd software/openobd/
python3 -m pytest
```

## Dependencies
Python packages (`pip3 install package-name`):
* `pytest` (doc.pytest.org/en/latest/)
* `RPi.GPIO` (https://pypi.python.org/pypi/RPi.GPIO)
* `PySerial` (https://pythonhosted.org/pyserial/)
* `python-can` (https://python-can.readthedocs.io)

## Contributors
* Nicholas Mulvenna
* Isaiah Thiessen
* Ehsan Ahmadi
* Kaibo Ma
* Rob Chartier
