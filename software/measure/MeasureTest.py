import Measure

def test_example():
	myMeasure = Measure.Measure(1,"metres", 2)
	assert myMeasure.getValue() == 1
	assert myMeasure.getUnits() == "metres"
	assert myMeasure.getTime() == 2
