import time

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin, SoftI2C
import ssd1306
from time import sleep

firmware_url = "https://github.com/SMHub/esp_mpy_ota/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

i2c = SoftI2C(scl=Pin(4), sda=Pin(5))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)
oled.text('CHECK----!', 0, 0)
oled.text('FOR!----', 0, 20)
oled.text('UPDATE!----', 0, 40)
oled.show()

while True:
    ota_updater.download_and_install_update_if_available()
    time.sleep(60)
    print("Hello World!")
    oled.fill(0)
    oled.text('----!', 0, 0)
    oled.text('WORKED!----', 0, 20)
    oled.text('5:43!----', 0, 40)
    oled.show()

# OLED


# ESP32 Pin assignment. Note: 4,5 for OLED with 18630



