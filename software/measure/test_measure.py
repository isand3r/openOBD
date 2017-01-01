from software.measure.measure import Measure
import datetime

def test_distance():
	value = 5
	units = "metres"
	time = datetime.datetime.now()
	distance = Measure(value, units, time)
	assert distance.value == value
	assert distance.units == units
	assert distance.time == time
