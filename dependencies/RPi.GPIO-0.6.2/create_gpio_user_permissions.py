import grp
import subprocess

def ensure_gpiogroup():
    try:
        grp.getgrnam('gpio')
    except KeyError:
        print('GPIO group does not exist - creating...')
        subprocess.call(['groupadd', '-f', '-r', 'gpio'])
        subprocess.call(['adduser', 'pi', 'gpio'])
        # in future, also for groups:
        #   spi
        #   i2c
        add_udev_rules()

def add_udev_rules():
    with open('/etc/udev/rules.d/99-gpio.rules','w') as f:
        f.write("""SUBSYSTEM=="bcm2835-gpiomem", KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'"
SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"
""")

if __name__ == '__main__':
    ensure_gpiogroup()
