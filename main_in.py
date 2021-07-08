import Jetson.GPIO as GPIO
import time

# Pin Definitions
gpio_pin = 35   #I2S0_FS BOARD GPIO 35


def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(gpio_pin, GPIO.IN)

    print("Press CTRL+C to exit")
    try:
        while True:
            time.sleep(1)
            curr_value = GPIO.input(gpio_pin)
            print("Input {} to pin {}".format(curr_value, gpio_pin))

    finally:
        GPIO.cleanup()



if __name__ == '__main__':
    main()