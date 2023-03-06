import os
import sys
import board
import busio
import adafruit_mlx90640
import adafruit_bme680
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

mlx_i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
bme_i2c = board.I2C()

try:
    mlx = adafruit_mlx90640.MLX90640(mlx_i2c)
    bme = adafruit_bme680.Adafruit_BME680_I2C(bme_i2c)
except ValueError as e:
    logger(f"Error while initalizing sensors: {e}", 1)
# print("MLX addr detected on I2C")
# print([hex(i) for i in mlx.serial_number])

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768
try: # make sure the lock file still gets deleted if manually stopped
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
    
    if LOCAL_LOGFILE:
        with open(f'{directory}/data/{get_date_string()}.log', 'a') as fp:
            timestamp = int(time.time())
            image = frame_array
            outside_temp = bme.temperature
            gas_ohms = bme.gas
            humidity_percent = bme.humidity
            pressure_hpa = bme.pressure

            fp.write(f'{timestamp}, {image}, {outside_temp}, {gas_ohms}, {humidity_percent}, {pressure_hpa}\n')

        # print(frame_array)
except KeyboardInterrupt:
    pass

# clean up
os.remove(lockfile_path)
            