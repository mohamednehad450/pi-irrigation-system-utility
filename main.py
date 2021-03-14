import atexit
import time

from config import load_config
from utils import exit_handler, GPIO_Initialize, run_zone

atexit.register(exit_handler)


def main():

    config = load_config('config.json')

    gpio = config.get('GPIOPins')
    GPIO_Initialize(gpio)

    zones = config.get('Zones')
    timeout = config.get('timeout')

    for zone in zones:
        run_zone(zone)
        time.sleep(timeout)


if __name__ == "__main__":
    main()
