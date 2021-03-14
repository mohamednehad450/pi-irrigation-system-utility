import json


def load_config(f):
    return validate_config(json.load(open(f, "r")))


def validate_config(config):

    gpio = config.get('GPIOPins')
    if gpio is None or not type(gpio) == list:
        raise RuntimeError('missing or invalid "GPIOPins".')

    zones = config.get('Zones')
    if zones is None or not type(zones) == list:
        raise RuntimeError('missing or invalid "Zones".')

    for zone in zones:
        validate_zone(zone, gpio)

    timeout = config.get('timeout')
    if timeout is None or not type(timeout) == int or timeout < 0:
        raise RuntimeError('missing or invalid "timeout".')

    return config


def validate_zone(zone, gpio):
    name = zone.get('name')
    if name is None or not type(name) == str:
        raise RuntimeError('All "Zones" must have a valid "name"')

    pins = zone.get("pins")
    if pins is None or not type(pins) == list:
        raise RuntimeError(f'missing or invalid pins (zone:"{name}").')

    for p in pins:
        pin = p.get('pin')
        if pin is None or not pin in gpio:
            raise RuntimeError(f'missing or invalid gpio pin (zone:"{name}").')

        duration = p.get('duration')
        if duration is None or not type(duration) == int or duration < 0:
            raise RuntimeError(
                f'missing or invalid pin duration (zone:"{name}").')

    pumpPin = zone.get('pumpPin')
    if pumpPin is not None:

        if not pumpPin in gpio:
            raise RuntimeError(f'Invalid pump pin (zone:"{name}").')

        pumpInitTime = zone.get('pumpInitTime')
        if pumpInitTime is None or not type(pumpInitTime) == int or pumpInitTime < 0:
            raise RuntimeError(
                f'Invalid pumpInitTime (zone:"{name}").')
