import atexit

from config import load_config
from utils import exit_handler

atexit.register(exit_handler)


def main():
    config = load_config('config.json')
    print(config)


if __name__ == "__main__":
    main()
