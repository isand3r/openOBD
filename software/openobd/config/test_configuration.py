from config.configuration import Configuration

def test_manager():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.manager_moving_average_items == 3
	assert config.manager_print_interval == 0.7

def test_obd():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.obd_device == 'test_obd_device'
	assert config.rpm_interval == 0.8
	assert config.speed_interval == 0.9

def test_gps():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.gps_device == 'test_gps_device'
	assert config.gps_interval == 1.1

def test_thermo():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.thermo_device == 'test_thermo_device'
	assert config.thermo_interval == 1.2

def test_accel():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.accel_device == 'test_accel_device'
	assert config.accel_interval == 1.3

def test_baro():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.baro_device == 'test_baro_device'
	assert config.baro_interval == 1.4

def test_volt():
	config = Configuration()
	config.read('config/test_config.ini')
	assert config.volt_device == 'test_volt_device'
	assert config.volt_interval == 1.5
