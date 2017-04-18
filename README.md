# openOBD
An open-source vehicle telemetry system based on the [Raspberry Pi 0](https://www.raspberrypi.org/blog/raspberry-pi-zero) that supports OBD-2 and includes several sensors
Originally developed as a UBC Electrical & Computer Engineering [Capstone Project](https://www.ece.ubc.ca/courses/capstones) for [Mojio](https://www.moj.io/)

![photo](https://raw.githubusercontent.com/isand3r/openOBD/master/docs/photo.jpg)

## Usage

### Command Line Application
```
python3 software/openobd/app.py
```

![screenshot](https://raw.githubusercontent.com/isand3r/openOBD/master/docs/screenshot.png)

### Configuration File
The configuration file `software/openobd/configuration/config.ini` (parsed using [configparser](https://docs.python.org/3/library/configparser.html)) is used to select the class that will be used for each sensor device (GPS, thermometer, etc). If mock devices are used (and if a few lines are commented out in `software/openobd/app.py`), the command line application can be run on a regular PC without requiring the openOBD hardware.

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
