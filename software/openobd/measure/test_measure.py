from measure.measure import Measure
import datetime

def test_distance():
	value = 5
	units = "metres"
	time = datetime.datetime.now()
	distance = Measure(value, units, time)
	assert distance.value == value
	assert distance.units == units
	assert distance.time == time

def test_average_distance():
	time0 = datetime.datetime.now()
	units0 = "metres"
	distance0 = Measure(5, units0, time0)
	distance1 = Measure(6, units0, time0)
	distance2 = Measure(12, units0, time0)
	distance3 = Measure(20, units0, time0)
	average_value = (5+6+12+20)/4
	distances = list()
	distances.append(distance0)
	distances.append(distance1)
	distances.append(distance2)
	distances.append(distance3)
	assert Measure.average_measure(distances).value == average_value
