import measure
import datetime

def test_distance():
	value = 5
	units = "metres"
	time = datetime.datetime.now()
	distance = measure.Measure(value, units, time)
	assert distance.value == value
	assert distance.units == units
	assert distance.time == time
