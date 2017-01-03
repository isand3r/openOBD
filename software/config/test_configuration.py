from software.config.configuration import Configuration

def test_read_gps_thermo():
	config = Configuration()
	config.read('config/config.ini')
	assert config.gps == 'fixed_mock'
	assert (config.thermo == 'fixed_mock') or (config.thermo == 'rising_mock')
