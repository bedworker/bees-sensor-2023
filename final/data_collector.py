import os
import sys
import board
import busio
import adafruit_mlx90640 # thermal camera
import adafruit_bme680   # pressure, temp sensor
import adafruit_tca9548a # multiplexer
import time

from common import logger, get_date_string

# Options
LOCAL_LOGFILE = True

directory = os.path.dirname(os.path.abspath(__file__))
lockfile_path = f'{__file__}.lock'
if os.path.exists(lockfile_path):
    logger("Lockfile exists!", 1)
else:
    # just create it
    open(lockfile_path, 'x').close()

# mlx_i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
i2c = board.I2C()
tca = adafruit_tca9548a.TCA9548A(i2c)

try:
    mlx1 = adafruit_mlx90640.MLX90640(tca[0])
    mlx2 = adafruit_mlx90640.MLX90640(tca[2])
    bme = adafruit_bme680.Adafruit_BME680_I2C(tca[1])
except ValueError as e:
    logger(f"Error while initalizing sensors: {e}", 1)
# print("MLX addr detected on I2C")
# print([hex(i) for i in mlx.serial_number])

images = []
for mlx in [mlx1, mlx2]:
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

    frame = [0] * 768
    stamp = time.monotonic()
    for i in range(5): # it gets 5 tries
        try:
            mlx.getFrame(frame)
            break
        except ValueError:
            # these happen, no biggie - retry
            continue

    print("Read 2 frames in %0.2f s" % (time.monotonic() - stamp))
    # start converting to array so we can log it
    frame_array = []
    for h in range(24):
        frame_line = []
        for w in range(32):
            frame_line.append(round(frame[h * 32 + w],4))
        frame_array.append(frame_line)
    
    images.append(frame_array)
    
if LOCAL_LOGFILE:
    with open(f'{directory}/data/{get_date_string()}.log', 'a') as fp:
        timestamp = int(time.time())
        outside_temp = bme.temperature
        gas_ohms = bme.gas
        humidity_percent = bme.humidity
        pressure_hpa = bme.pressure    
        #                          mlx1         mlx2
        fp.write(f'{timestamp}, {images[0]}, {images[1]}, {outside_temp}, {gas_ohms}, {humidity_percent}, {pressure_hpa}\n')

    # print(frame_array)

# clean up
os.remove(lockfile_path)
            