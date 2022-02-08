def connectToWifiAndUpdate():
    import time, machine, network, gc
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from app.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("EXP", "201060dx")
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    otaUpdater = OTAUpdater('https://github.com/guzov-afk/ESP/edit/main/', files = "boot.py")
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del(otaUpdater)
        gc.collect()




connectToWifiAndUpdate()

import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

while True:
    led.value(1)






