from accumulator.accumulator import Accumulator
from measure.measure import Measure
import datetime

def test_name():
	name = "test"
	capacity = 2
	accumulator = Accumulator(name, capacity)
	assert accumulator.name == name

def test_empty_clear():
	"""Test the empty property and clear method"""
	name = "test"
	capacity = 2
	accumulator = Accumulator(name, capacity)
	assert accumulator.empty
	value = 1
	units = "metres"
	time = datetime.datetime.now()
	measure = Measure(value, units, time)
	accumulator.push(measure)
	assert not accumulator.empty
	accumulator.clear()
	assert accumulator.empty

def test_newest():
	time0 = datetime.datetime.now()
	units = "metres"
	distance0 = Measure(5, units, time0)
	distance1 = Measure(6, units, time0)
	name = "distance"
	capacity = 5
	accumulator = Accumulator(name, capacity)
	accumulator.push(distance0)
	accumulator.push(distance1)
	assert accumulator.newest().value == distance1.value

def test_mean():
	"""Test the mean() method and test that the correct capacity is used"""
	time = datetime.datetime.now()
	units = "metres"
	distance0 = Measure(5, units, time)
	distance1 = Measure(6, units, time)
	distance2 = Measure(12, units, time)
	distance3 = Measure(20, units, time)
	average_value = (5+6+12+20)/4
	name = "distance"
	capacity = 5
	accumulator = Accumulator(name, capacity)
	accumulator.push(distance0)
	accumulator.push(distance1)
	accumulator.push(distance2)
	accumulator.push(distance3)
	assert accumulator.mean().value == average_value
	# push more entries to check that the previous entries are dropped
	# once we go over the accumulator's capacity
	distance4 = Measure(1, units, time)
	distance5 = Measure(1, units, time)
	distance6 = Measure(1, units, time)
	distance7 = Measure(1, units, time)
	distance8 = Measure(1, units, time)
	accumulator.push(distance4)
	accumulator.push(distance5)
	accumulator.push(distance6)
	accumulator.push(distance7)
	accumulator.push(distance8)
	assert accumulator.mean().value == 1

def test_median():
	time = datetime.datetime.now()
	units = "metres"
	distance0 = Measure(5, units, time)
	distance1 = Measure(6, units, time)
	distance2 = Measure(12, units, time)
	distance3 = Measure(20, units, time)
	name = "distance"
	capacity = 5
	accumulator = Accumulator(name, capacity)
	accumulator.push(distance0)
	accumulator.push(distance1)
	accumulator.push(distance2)
	accumulator.push(distance3)
	# use the upper middle measure if there are an even number
	assert accumulator.median().value == 12

def test_minimum_maximum():
	"""Test the minimum and maximum methods"""
	time0 = datetime.datetime.now()
	units = "metres"
	distance0 = Measure(5, units, time0)
	distance1 = Measure(6, units, time0)
	distance2 = Measure(4, units, time0)
	name = "distance"
	capacity = 5
	accumulator = Accumulator(name, capacity)
	accumulator.push(distance0)
	accumulator.push(distance1)
	accumulator.push(distance2)
	assert accumulator.minimum().value == distance2.value
	assert accumulator.maximum().value == distance1.value
