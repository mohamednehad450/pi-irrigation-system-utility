import time
from functools import reduce

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("couldn't import RPi.GPIO module, try again with sudo")
except ModuleNotFoundError:
    print(f'MOCK: couldn\'t find RPi.GPIO module, Using mock module instead.')
    from mockGPIO import GPIO


def log_with_timestamp(message, f, mode="a"):

    m = f"[{time.ctime()}]: {message} \n"

    log = open(f, mode)
    log.write(m)
    log.close()

    return m


def GPIO_Initialize(gpio, mode=GPIO.BOARD):

    GPIO.setmode(mode)

    for pin in gpio:
        GPIO.setup(pin, GPIO.OUT, initial=1)


def turn_on(pin):
    GPIO.output(pin, GPIO.LOW)


def turn_off(pin):
    GPIO.output(pin, GPIO.HIGH)


def exit_handler():
    GPIO.cleanup()


def run_config(config, logger):
    # TODO
    pass
