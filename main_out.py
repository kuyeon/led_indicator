import Jetson.GPIO as GPIO
import time

"""
No.      1.8V      PIN_NUMBER
1     I2S0_DIN         38
2     I2S0_DOUT        40
3     I2DS0_FS         35
4     I2S0_SCLK        12
5     SPI1_SCK         13
6     SPI1_MISO        22
7     SPI1_MOSI        37
8     SPI1_CS0         18
9     SPI1_CS1         16
"""
I2S0_DIN = 38
I2S0_DOUT = 40
I2S0_FS = 35
I2S0_SCLK = 12
SPI1_SCK = 13
SPI1_MISO = 22
SPI1_MOSI = 37
SPI1_CS0 = 18
SPI1_CS1 = 16


pins = [SPI1_SCK, SPI1_MISO, SPI1_MOSI, SPI1_CS0, SPI1_CS1,
        I2S0_DIN, I2S0_DOUT, I2S0_FS, I2S0_SCLK]


GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.TEGRA_SOC)
# GPIO.setmode(GPIO.BCM)

SLEEP_RATE = 0.05

def setup_pins_to_output(pins_list):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)


def led_high():
    global pins
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        print("outputting {}: GPIO HIGH".format(pin))
        time.sleep(SLEEP_RATE)


def led_low():
    global pins
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        print("outputting {}: GPIO LOW".format(pin))
        time.sleep(SLEEP_RATE)


def reverse_led_high():
    global pins
    for pin in pins[::-1]:
        GPIO.output(pin, GPIO.HIGH)
        print("outputting {}: GPIO HIGH".format(pin))
        time.sleep(SLEEP_RATE)


def reverse_led_low():
    global pins
    for pin in pins[::-1]:
        GPIO.output(pin, GPIO.LOW)
        print("outputting {}: GPIO LOW".format(pin))
        time.sleep(SLEEP_RATE)


def main():
    # Pin Setup:
    setup_pins_to_output(pins)

    # set pin as an output pin with optional initial state of HIGH
    print("Press CTRL+C to exit")
    try:
        while True:
            led_high()
            reverse_led_low()
            reverse_led_high()
            led_low()
            # Toggle the output every second
    finally:
        for pin in pins:
            GPIO.output(pin, False)
            time.sleep(0.01)
        GPIO.cleanup()


if __name__ == '__main__':
    main()


