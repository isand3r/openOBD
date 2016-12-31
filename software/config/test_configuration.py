import configuration

def test_read_gps_thermo():
	config = configuration.Configuration()
	config.read('config.ini')
	assert config.gps == 'mock'
	assert config.thermo == 'mock'
