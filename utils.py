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


def get_min_duration(pins):
    if len(pins) > 0:
        return reduce(lambda acc, pin: min(acc, pin.get('duration')), pins, pins[0].get('duration'))
    else:
        return 0


def run_zone(zone, log):

    name = zone.get('name')
    pins = zone.get('pins')
    pumpPin = zone.get('pumpPin')
    pumpInitTime = zone.get('pumpInitTime')

    log(f'Zone "{name}": Starting.')
    # turning on every pin
    for pin in pins:
        log(f'Zone "{name}": Pin {pin.get("pin")} will start for {pin.get("duration")}min.')
        turn_on(pin.get("pin"))

    # turning on the pump
    if pumpPin:
        time.sleep(pumpInitTime)
        log(f'Zone "{name}": Pump will start on pin {pumpPin}.')
        turn_on(pumpPin)

    while len(pins) > 0:

        minDuration = get_min_duration(pins)
        time.sleep(minDuration*60)

        # Subtracting minDuration from all pins
        pins = list(
            map(lambda pin: {**pin, "duration": pin.get('duration') - minDuration}, pins))

        # Filtering finished pins
        # filteredPins = list(filter(lambda pin: pin.get('duration') > 0, pins))
        filteredPins = [pin for pin in pins if pin.get('duration') > 0]

        # Turning off the pump if all pins finished
        if len(filteredPins) == 0 and pumpPin:
            log(f'Zone "{name}": Pump will stop now.')
            turn_off(pumpPin)
            time.sleep(pumpInitTime)

        # turning off done pins
        for pin in pins:
            if pin.get('duration') <= 0:
                log(f'Zone "{name}": Pin {pin.get("pin")} will stop now.')
                turn_off(pin.get("pin"))

        pins = filteredPins

        # set minDuration
        minDuration = get_min_duration(pins)

    log(f'Zone "{name}": Done.')
