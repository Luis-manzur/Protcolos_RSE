import RPi.GPIO as GPIO
from time import sleep, time

class Status_Reader:
    """A class that watch the status from the antenna."""

    def __init__(self, gpio_0, gpio_1):

        self.gpio_0 = gpio_0
        self.gpio_1 = gpio_1
        """Initialization class."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_0, GPIO.IN)
        GPIO.setup(self.gpio_1, GPIO.IN)

    def status(self):
        """Read the status every 2 seconds"""
        if GPIO.input(self.gpio_0) == 0:
            if GPIO.input(self.gpio_1) == 0:
                print("La antena esta desconectada")

        if GPIO.input(self.gpio_1) == 0:
            if GPIO.input(self.gpio_0) == 0:
                print("La antena esta desconectada")
        sleep(2)
        self.status()

