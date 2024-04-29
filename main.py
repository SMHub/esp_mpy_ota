# ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")
# ota_updater.download_and_install_update_if_available()
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD


firmware_url = "https://github.com/SMHub/esp_mpy_ota/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

print("Hello World!")

