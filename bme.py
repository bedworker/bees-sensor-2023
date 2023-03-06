import board
import adafruit_bme680
import time

i2c = board.I2C()
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
while True:
    try:
        print('Temperature: {} degrees C'.format(sensor.temperature))
        print('Gas: {} ohms'.format(sensor.gas))
        print('Humidity: {}%'.format(sensor.humidity))
        print('Pressure: {}hPa'.format(sensor.pressure))
        print('Altitude: {}m'.format(sensor.altitude))
        print()

        time.sleep(1)
    except KeyboardInterrupt:
        break