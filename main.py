import atexit
import json

from utils import exit_handler

atexit.register(exit_handler)


def main():
    configFile = open('config.json', "r")
    config = json.load(configFile)
    print(config)


if __name__ == "__main__":
    main()
