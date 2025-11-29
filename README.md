# nrf24l01-bt-jammer
This is a simple setup that can jam bt classic completely but can only disrupt BLE connections as it uses adaptive frequency hopping so this can only sweep frequencies in the 2.4 Ghz band. I have used a raspberry pi pico WH and the nrf24l01+pa+lna comm module for CW transmission. You can optionaly use the ssd1306 module for errors as i have used but if you are not, then you have to modify the main block of code in the main.py file.<br>

<img src="https://github.com/user-attachments/assets/23385426-a4fe-40c0-a9ad-4d94741d94d4" alt="hwd" width="270"/>


---
## Hardware 
- raspberry pi pico wh
- nrf24l01 module
- ssd1306 oled (optional)<br>

### pin connection
|       NRF24L01       |        Pico wh       |
|----------------------|----------------------|
|        VCC           |       3V3 Pin 40     |
|        CSN           |       GP14	Pin 19    |
|        CE            |       GP17	Pin 22    |
|        SCK           |       GP10	Pin 14    |
|        MOSI          |       GP11	Pin 15    |
|        MISO	         |       GP12	Pin 16    | 

---
ssd1306 connection: <br>
This is optional but for displaying if the nrf24l01 module is working i have used this module for display.<br>
|            Pico WH           | SSD1306 & 1602 LCD |
|------------------------------|--------------------|
| VBUS (Pin 40) or 3V3 (Pin 36) | VCC                |
| GND (Pin 38)                 | GND                |
| GPIO4 (Pin 6)                | SDA (Data Line)    |
| GPIO5 (Pin 7)                | SCL (Clock Line)   |

---
## Thony
After configuring the hardware connect the pico to your pc by holding the bootsell button. COpy and past the `nrf24l01.py` and `main.py` to the root dir of the pico and also install the ssd1306 oled driver lib if you are using the module. then test by running the main.py file.
