from mpu6050 import mpu6050

class Impu6050Temp:

  def receive(self):
    init = mpu6050(0x68)   
    return mpu6050.get_temp(init)

class Impu6050Accel:
  
  def receive(self):
    init = mpu6050(0x68)   
    return mpu6050.get_accel_data(init)
    
class Impu6050Gyro:
  
  def receive(self):
    init = mpu6050(0x68)
    return mpu6050.get_gyro_data(init)
