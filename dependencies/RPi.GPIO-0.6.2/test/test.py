#!/usr/bin/env python2
"""
Copyright (c) 2013-2016 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""This test suite assumes the following circuit is connected:
GND_PIN = 6
LED_PIN = 12 (with resistor to 0v)
SWITCH_PIN = 18 (with 0.1 uF capacitor around switch) to 0v
LOOP_IN = 16 connected with 1K resistor to LOOP_OUT
LOOP_OUT = 22
"""

import sys
import warnings
import time
from threading import Timer
import RPi.GPIO as GPIO
if sys.version[:3] == '2.6':
    import unittest2 as unittest
else:
    import unittest

GND_PIN = 6
LED_PIN = 12
LED_PIN_BCM = 18
SWITCH_PIN = 18
LOOP_IN = 16
LOOP_OUT = 22

non_interactive = False
for i,val in enumerate(sys.argv):
    if val == '--non_interactive':
        non_interactive = True
        sys.argv.pop(i)

# Test starts with 'AAA' so that it is run first
class TestAAASetup(unittest.TestCase):
    def runTest(self):
        # Test mode not set (BOARD or BCM) exception
        with self.assertRaises(RuntimeError) as e:
            GPIO.setup(LED_PIN, GPIO.OUT)
        self.assertEqual(str(e.exception), 'Please set pin numbering mode using GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)')

        # Test trying to change mode after it has been set
        GPIO.setmode(GPIO.BCM)
        with self.assertRaises(ValueError) as e:
            GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_PIN_BCM, GPIO.IN)
        GPIO.cleanup()

        # Test setting an invalid mode
        with self.assertRaises(ValueError):
            GPIO.setmode(666)

        # Test getmode()
        self.assertEqual(GPIO.getmode(), None)
        GPIO.setmode(GPIO.BCM)
        self.assertEqual(GPIO.getmode(), GPIO.BCM)
        GPIO.setup(LED_PIN_BCM, GPIO.IN)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.getmode(), GPIO.BOARD)

        # Test not set as OUTPUT message
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(RuntimeError) as e:
            GPIO.output(LED_PIN, GPIO.HIGH)
        self.assertEqual(str(e.exception), 'The GPIO channel has not been set up as an OUTPUT')

        # Test setup(..., pull_up_down=GPIO.HIGH) raises exception
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(ValueError):
            GPIO.setup(LED_PIN, GPIO.IN, pull_up_down=GPIO.HIGH)

        # Test not valid on a raspi exception
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(ValueError) as e:
            GPIO.setup(GND_PIN, GPIO.OUT)
        self.assertEqual(str(e.exception), 'The channel sent is invalid on a Raspberry Pi')

        # Test 'already in use' warning
        GPIO.setmode(GPIO.BOARD)
        with open('/sys/class/gpio/export','wb') as f:
            f.write(str(LED_PIN_BCM).encode())
        time.sleep(0.2)  # wait for udev to set permissions
        with open('/sys/class/gpio/gpio%s/direction'%LED_PIN_BCM,'wb') as f:
            f.write(b'out')
        time.sleep(0.2)
        with warnings.catch_warnings(record=True) as w:
            GPIO.setup(LED_PIN, GPIO.OUT)    # generate 'already in use' warning
            self.assertEqual(w[0].category, RuntimeWarning)
        with open('/sys/class/gpio/unexport','wb') as f:
            f.write(str(LED_PIN_BCM).encode())
        GPIO.cleanup()

        # test initial value of high reads back as high
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.HIGH)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.HIGH)
        GPIO.cleanup()

        # test initial value of low reads back as low
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.LOW)
        GPIO.cleanup()

        # test setup of a list of channels
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup( [LED_PIN, LOOP_OUT], GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.OUT)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(ValueError) as e:
            GPIO.setup( [LED_PIN, GND_PIN], GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        self.assertEqual(str(e.exception), 'The channel sent is invalid on a Raspberry Pi')
        GPIO.cleanup()

        # test setup of a tuple of channels
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup( (LED_PIN, LOOP_OUT), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.OUT)
        GPIO.cleanup()

        # test warning when using pull up/down on i2c channels
        GPIO.setmode(GPIO.BOARD)
        if GPIO.RPI_INFO['P1_REVISION'] == 0: # compute module
            pass    # test not vailid
        else:  # revision 1, 2 or A+/B+
            with warnings.catch_warnings(record=True) as w:
                GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                self.assertEqual(w[0].category, RuntimeWarning)
            with warnings.catch_warnings(record=True) as w:
                GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                self.assertEqual(w[0].category, RuntimeWarning)
            GPIO.cleanup()

        # test non integer channel
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(ValueError):
            GPIO.setup('d', GPIO.OUT)
        with self.assertRaises(ValueError):
            GPIO.setup(('d',LED_PIN), GPIO.OUT)

        # test setting pull_up_down on an output
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(ValueError):
            GPIO.setup(LOOP_OUT, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

        # test setting initial on an input
        GPIO.setmode(GPIO.BOARD)
        with self.assertRaises(ValueError):
            GPIO.setup(LOOP_IN, GPIO.IN, initial=GPIO.LOW)

class TestInputOutput(unittest.TestCase):
    def setUp(self):
        GPIO.setmode(GPIO.BOARD)

    def test_outputread(self):
        """Test that an output() can be input()"""
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.HIGH)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.HIGH)
        GPIO.output(LED_PIN, GPIO.LOW)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.LOW)

    def test_loopback(self):
        """Test output loops back to another input"""
        GPIO.setup(LOOP_IN, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        GPIO.setup(LOOP_OUT, GPIO.OUT, initial=GPIO.LOW)
        self.assertEqual(GPIO.input(LOOP_IN), GPIO.LOW)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        self.assertEqual(GPIO.input(LOOP_IN), GPIO.HIGH)

    def test_output_on_input(self):
        """Test output() can not be done on input"""
        GPIO.setup(SWITCH_PIN, GPIO.IN)
        with self.assertRaises(RuntimeError):
            GPIO.output(SWITCH_PIN, GPIO.LOW)

    def test_output_list(self):
        """Test output() using lists"""
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)

        GPIO.output( [LOOP_OUT, LED_PIN], GPIO.HIGH)
        self.assertEqual(GPIO.input(LOOP_OUT), GPIO.HIGH)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.HIGH)

        GPIO.output( (LOOP_OUT, LED_PIN), GPIO.LOW)
        self.assertEqual(GPIO.input(LOOP_OUT), GPIO.LOW)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.LOW)

        GPIO.output( [LOOP_OUT, LED_PIN], [GPIO.HIGH, GPIO.LOW] )
        self.assertEqual(GPIO.input(LOOP_OUT), GPIO.HIGH)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.LOW)

        GPIO.output( (LOOP_OUT, LED_PIN), (GPIO.LOW, GPIO.HIGH) )
        self.assertEqual(GPIO.input(LOOP_OUT), GPIO.LOW)
        self.assertEqual(GPIO.input(LED_PIN), GPIO.HIGH)

        with self.assertRaises(RuntimeError):
            GPIO.output( [LOOP_OUT, LED_PIN], [0,0,0] )

        with self.assertRaises(RuntimeError):
            GPIO.output( [LOOP_OUT, LED_PIN], (0,) )

        with self.assertRaises(RuntimeError):
            GPIO.output(LOOP_OUT, (0,0))

        with self.assertRaises(ValueError):
            GPIO.output( [LOOP_OUT, 'x'], (0,0) )

        with self.assertRaises(ValueError):
            GPIO.output( [LOOP_OUT, LED_PIN], (0,'x') )

        with self.assertRaises(ValueError):
            GPIO.output( [LOOP_OUT, GND_PIN], (0,0) )

        with self.assertRaises(RuntimeError):
            GPIO.output( [LOOP_OUT, LOOP_IN], (0,0) )

    def tearDown(self):
        GPIO.cleanup()

class TestSoftPWM(unittest.TestCase):
    @unittest.skipIf(non_interactive, 'Non interactive mode')
    def runTest(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_PIN, GPIO.OUT)
        pwm = GPIO.PWM(LED_PIN, 50)
        pwm.start(100)
        print "\nPWM tests"
        response = raw_input('Is the LED on (y/n) ? ').upper()
        self.assertEqual(response,'Y')
        pwm.start(0)
        response = raw_input('Is the LED off (y/n) ? ').upper()
        self.assertEqual(response,'Y')
        print "LED Brighten/fade test..."
        for i in range(0,3):
            for x in range(0,101,5):
                pwm.ChangeDutyCycle(x)
                time.sleep(0.1)
            for x in range(100,-1,-5):
                pwm.ChangeDutyCycle(x)
                time.sleep(0.1)
        pwm.stop()
        response = raw_input('Did it work (y/n) ? ').upper()
        self.assertEqual(response,'Y')
        GPIO.cleanup()

class TestSetWarnings(unittest.TestCase):
    def test_alreadyinuse(self):
        """Test 'already in use' warning"""
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        with open('/sys/class/gpio/export','wb') as f:
            f.write(str(LED_PIN_BCM).encode())
        time.sleep(0.2)  # wait for udev to set permissions
        with open('/sys/class/gpio/gpio%s/direction'%LED_PIN_BCM,'wb') as f:
            f.write(b'out')
        with warnings.catch_warnings(record=True) as w:
            GPIO.setup(LED_PIN, GPIO.OUT)    # generate 'already in use' warning
            self.assertEqual(len(w),0)       # should be no warnings
        with open('/sys/class/gpio/unexport','wb') as f:
            f.write(str(LED_PIN_BCM).encode())
        GPIO.cleanup()

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(True)
        with open('/sys/class/gpio/export','wb') as f:
            f.write(str(LED_PIN_BCM).encode())
        time.sleep(0.2)  # wait for udev to set permissions
        with open('/sys/class/gpio/gpio%s/direction'%LED_PIN_BCM,'wb') as f:
            f.write(b'out')
        with warnings.catch_warnings(record=True) as w:
            GPIO.setup(LED_PIN, GPIO.OUT)    # generate 'already in use' warning
            self.assertEqual(w[0].category, RuntimeWarning)
        with open('/sys/class/gpio/unexport','wb') as f:
            f.write(str(LED_PIN_BCM).encode())
        GPIO.cleanup()

    def test_cleanupwarning(self):
        """Test initial GPIO.cleanup() produces warning"""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SWITCH_PIN, GPIO.IN)
        with warnings.catch_warnings(record=True) as w:
            GPIO.cleanup()
            self.assertEqual(len(w),0) # no warnings
            GPIO.cleanup()
            self.assertEqual(len(w),0) # no warnings

        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SWITCH_PIN, GPIO.IN)
        with warnings.catch_warnings(record=True) as w:
            GPIO.cleanup()
            self.assertEqual(len(w),0) # no warnings
            GPIO.cleanup()
            self.assertEqual(w[0].category, RuntimeWarning) # a warning

class TestVersions(unittest.TestCase):
    def test_rpi_info(self):
        print 'RPi Board Information'
        print '---------------------'
        for key,val in GPIO.RPI_INFO.items():
            print '%s => %s'%(key,val)
        response = raw_input('\nIs this board info correct (y/n) ? ').upper()
        self.assertEqual(response, 'Y')

    def test_gpio_version(self):
        response = raw_input('\nRPi.GPIO version %s - is this correct (y/n) ? '%GPIO.VERSION).upper()
        self.assertEqual(response, 'Y')

class TestGPIOFunction(unittest.TestCase):
    def runTest(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN_BCM, GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN_BCM), GPIO.IN)
        GPIO.setup(LED_PIN_BCM, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN_BCM), GPIO.OUT)
        GPIO.cleanup()

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_PIN, GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)
        GPIO.setup(LED_PIN, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)

    def tearDown(self):
        GPIO.cleanup()

class TestSwitchBounce(unittest.TestCase):
    def __init__(self, *a, **k):
        unittest.TestCase.__init__(self, *a, **k)
        self.switchcount = 0

    def cb(self,chan):
        self.switchcount += 1
        print 'Button press',self.switchcount

    def setUp(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @unittest.skipIf(non_interactive, 'Non interactive mode')
    def test_switchbounce(self):
        self.switchcount = 0
        print "\nSwitch bounce test.  Press switch at least 10 times and count..."
        GPIO.add_event_detect(SWITCH_PIN, GPIO.FALLING, callback=self.cb, bouncetime=200)
        while self.switchcount < 10:
            time.sleep(1)
        GPIO.remove_event_detect(SWITCH_PIN)

    @unittest.skipIf(non_interactive, 'Non interactive mode')
    def test_event_detected(self):
        self.switchcount = 0
        print "\nGPIO.event_detected() switch bounce test.  Press switch at least 10 times and count..."
        GPIO.add_event_detect(SWITCH_PIN, GPIO.FALLING, bouncetime=200)
        while self.switchcount < 10:
            if GPIO.event_detected(SWITCH_PIN):
                self.switchcount += 1
                print 'Button press',self.switchcount
        GPIO.remove_event_detect(SWITCH_PIN)

    def tearDown(self):
        GPIO.cleanup()

class TestEdgeDetection(unittest.TestCase):
    def setUp(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LOOP_IN, GPIO.IN)
        GPIO.setup(LOOP_OUT, GPIO.OUT)

    def testWaitForEdgeInLoop(self):
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)

        count = 0
        timestart = time.time()
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        while True:
            t = Timer(0.1, makelow)
            t.start()
            GPIO.wait_for_edge(LOOP_IN, GPIO.FALLING)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            count += 1
            if time.time() - timestart > 5 or count > 150:
                break

    def testWaitForEdgeWithCallback(self):
        def cb():
            raise Exception("Callback should not be called")
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)

        GPIO.output(LOOP_OUT, GPIO.LOW)
        t = Timer(0.1, makehigh)

        GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        t.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)

        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_callback(LOOP_IN, callback=cb)
        with self.assertRaises(RuntimeError):   # conflicting edge exception
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)

        GPIO.remove_event_detect(LOOP_IN)

    def testWaitForEventSwitchbounce(self):
        self.finished = False
        def bounce():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            self.finished = True

        GPIO.output(LOOP_OUT, GPIO.LOW)
        t1 = Timer(0.1, bounce)
        t1.start()

        starttime = time.time()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=100)
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=100)
        finishtime = time.time()
        self.assertGreater(finishtime-starttime, 0.2)
        while not self.finished:
            time.sleep(0.1)

    def testInvalidBouncetime(self):
        with self.assertRaises(ValueError):
            GPIO.add_event_detect(LOOP_IN, GPIO.RISING, bouncetime=-1)
        with self.assertRaises(ValueError):
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=-1)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING, bouncetime=123)
        with self.assertRaises(RuntimeError):
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, bouncetime=321)
        GPIO.remove_event_detect(LOOP_IN)

    def testAlreadyAdded(self):
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        with self.assertRaises(RuntimeError):
            GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        GPIO.remove_event_detect(LOOP_IN)

    def testHighLowEvent(self):
        with self.assertRaises(ValueError):
            GPIO.add_event_detect(LOOP_IN, GPIO.LOW)
        with self.assertRaises(ValueError):
            GPIO.add_event_detect(LOOP_IN, GPIO.HIGH)

    def testFallingEventDetected(self):
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        GPIO.add_event_detect(LOOP_IN, GPIO.FALLING)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.remove_event_detect(LOOP_IN)

    def testRisingEventDetected(self):
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.remove_event_detect(LOOP_IN)

    def testBothEventDetected(self):
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.BOTH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        self.assertEqual(GPIO.event_detected(LOOP_IN), False)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        time.sleep(0.01)
        self.assertEqual(GPIO.event_detected(LOOP_IN), True)
        GPIO.remove_event_detect(LOOP_IN)

    def testWaitForRising(self):
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        t = Timer(0.1, makehigh)
        t.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)

    def testWaitForFalling(self):
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        t = Timer(0.1, makelow)
        t.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.FALLING)

    def testExceptionInCallback(self):
        self.run_cb = False
        def cb(channel):
            with self.assertRaises(ZeroDivisionError):
                self.run_cb = True
                a = 1/0
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING, callback=cb)
        time.sleep(0.01)
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        time.sleep(0.01)
        self.assertEqual(self.run_cb, True)
        GPIO.remove_event_detect(LOOP_IN)

    def testAddEventCallback(self):
        def cb(channel):
            self.callback_count += 1

        # falling test
        self.callback_count = 0
        GPIO.output(LOOP_OUT, GPIO.HIGH)
        GPIO.add_event_detect(LOOP_IN, GPIO.FALLING)
        GPIO.add_event_callback(LOOP_IN, cb)
        time.sleep(0.01)
        for i in range(2048):
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.001)
        GPIO.remove_event_detect(LOOP_IN)
        self.assertEqual(self.callback_count, 2048)

        # rising test
        self.callback_count = 0
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.RISING, callback=cb)
        time.sleep(0.01)
        for i in range(2048):
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.001)
        GPIO.remove_event_detect(LOOP_IN)
        self.assertEqual(self.callback_count, 2048)

        # both test
        self.callback_count = 0
        GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.add_event_detect(LOOP_IN, GPIO.BOTH, callback=cb)
        time.sleep(0.01)
        for i in range(2048):
            GPIO.output(LOOP_OUT, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(LOOP_OUT, GPIO.LOW)
            time.sleep(0.001)
        GPIO.remove_event_detect(LOOP_IN)
        self.assertEqual(self.callback_count, 4096)

    def testEventOnOutput(self):
        with self.assertRaises(RuntimeError):
            GPIO.add_event_detect(LOOP_OUT, GPIO.FALLING)

    def testAlternateWaitForEdge(self):
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)
        GPIO.output(LOOP_OUT, GPIO.LOW)
        t = Timer(0.1, makehigh)
        t2 = Timer(0.15, makelow)
        t.start()
        t2.start()
        GPIO.wait_for_edge(LOOP_IN, GPIO.RISING)
        GPIO.wait_for_edge(LOOP_IN, GPIO.FALLING)

    def testWaitForEdgeTimeout(self):
        def makehigh():
            GPIO.output(LOOP_OUT, GPIO.HIGH)
        def makelow():
            GPIO.output(LOOP_OUT, GPIO.LOW)

        with self.assertRaises(TypeError):
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, timeout="beer")

        with self.assertRaises(ValueError):
            GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, timeout=-1234)

        makelow()
        chan = GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, timeout=200)
        self.assertEqual(chan, None)

        t = Timer(0.1, makehigh)
        t.start()
        chan = GPIO.wait_for_edge(LOOP_IN, GPIO.RISING, timeout=200)
        self.assertEqual(chan, LOOP_IN)

    def tearDown(self):
        GPIO.cleanup()

class TestCleanup(unittest.TestCase):
    def setUp(self):
        GPIO.setmode(GPIO.BOARD)

    def test_cleanall(self):
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)

    def test_cleanone(self):
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup(LOOP_OUT)
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup(LED_PIN)
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)

    def test_cleantuple(self):
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup((LOOP_OUT,))
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup((LED_PIN,))
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.cleanup((LOOP_OUT,LED_PIN))
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)

    def test_cleanlist(self):
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.OUT)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup([LOOP_OUT])
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.OUT)
        GPIO.cleanup([LED_PIN])
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)
        GPIO.setup(LOOP_OUT, GPIO.OUT)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.cleanup([LOOP_OUT,LED_PIN])
        self.assertEqual(GPIO.gpio_function(LOOP_OUT), GPIO.IN)
        self.assertEqual(GPIO.gpio_function(LED_PIN), GPIO.IN)

if __name__ == '__main__':
    unittest.main()
