#do not change anything in this script
import ustruct as struct
from machine import SPI, Pin
from micropython import const
import utime

CONFIG      = const(0x00)
EN_AA       = const(0x01)
EN_RXADDR   = const(0x02)
SETUP_AW    = const(0x03)
SETUP_RETR  = const(0x04)
RF_CH       = const(0x05)
RF_SETUP    = const(0x06)
STATUS      = const(0x07)
RX_PW_P0    = const(0x11)
FIFO_STATUS = const(0x17)
DYNPD       = const(0x1C)
FEATURE     = const(0x1D)

class NRF24L01:
    def __init__(self, spi, csn, ce, payload_size=32):
        self.spi = spi
        self.csn = csn
        self.ce = ce
        self.payload_size = payload_size
        self.csn.value(1)
        self.ce.value(0)
        utime.sleep_ms(100) 
        self.setup()

    def reg_write(self, reg, value):
        self.csn.value(0)
        self.spi.write(bytes([0x20 | reg, value]))
        self.csn.value(1)

    def reg_read(self, reg):
        self.csn.value(0)
        self.spi.write(bytes([reg]))
        data = self.spi.read(1)
        self.csn.value(1)
        return data[0]

    def setup(self):
        self.reg_write(CONFIG, 0x0A) 
        utime.sleep_ms(5)
        self.reg_write(EN_AA, 0x00)
        self.reg_write(EN_RXADDR, 0x00)
        self.reg_write(SETUP_AW, 0x03)
        self.reg_write(SETUP_RETR, 0x00)
        self.reg_write(RF_SETUP, 0x06)   
        self.reg_write(DYNPD, 0x00)
        self.reg_write(FEATURE, 0x00)
        self.csn.value(0)
        self.spi.write(b'\xE1')
        self.csn.value(1)
        self.csn.value(0)
        self.spi.write(b'\xE2')
        self.csn.value(1)
        self.ce.value(1)

    def set_channel(self, channel):
        if channel < 0 or channel > 125:
            channel = 125
        self.reg_write(RF_CH, channel)

    def set_continuous_wave(self):
        self.ce.value(0)
        self.reg_write(RF_SETUP, 0x90 | 0x06) 
        self.ce.value(1)
