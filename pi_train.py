from mpu6050 import mpu6050 # import the library for the accelerometer/gyro
from time import sleep      # import the sleep (wait) command from the time library

sensor = mpu6050(0x68)

# Accelerometer measures position, by measuring gravity (essentially)
# Gyroscope measures rotational movement

while True:                                         # loop continuously
    accelerometer_data = sensor.get_accel_data()    # read the sensor
    
    gyro_data = sensor.get_gyro_data()

    xorient = accelerometer_data['x']               # put the x-axis position data into its own variable
    yorient = accelerometer_data['y']               # put the y-axis position data into its own variable
    zorient = accelerometer_data['z']               # put the z-axis position data into its own variable
    xrot = gyro_data['x']                           # put the x-axis rotation data into its own variable
    yrot = gyro_data['y']                           # put the y-axis rotation data into its own variable
    zrot = gyro_data['z']                           # put the z-axis rotation data into its own variable
                                                    # print out the data!
    print('Orientation:', xorient, ' | ', yorient, ' | ', zorient)
    print('Rotation:   ', xrot, ' | ', yrot, ' | ', zrot)
    sleep(1)                                        # Wait one second