from ..config.configuration import Configuration

def test_read_gps_thermo():
	config = Configuration()
	config.read('config/config.ini')
	assert (config.obd == 'obd')
	assert (config.gps == 'fixed_mock') or (config.gps == 'gps3')
	assert (config.thermo == 'fixed_mock') or (config.thermo == 'rising_mock') or (config.thermo =='mpu')
	assert (config.accel == 'fixed_mock') or (config.accel =='mpu')
