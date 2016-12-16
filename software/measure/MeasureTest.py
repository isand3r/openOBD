import Measure
import datetime

def test_distance():
	value = 5
	units = "metres"
	time = datetime.datetime.now()
	distance = Measure.Measure(value, units, time)
	assert distance.getValue() == value
	assert distance.getUnits() == units
	assert distance.getTime() == time
