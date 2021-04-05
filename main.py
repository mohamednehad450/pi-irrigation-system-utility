import atexit
import time

from config import load_config
from utils import log_with_timestamp, run_config


logfile = 'log.txt'
def logger(m): log_with_timestamp(m, logfile)


def main():

    config = load_config('config.json', 'schema.json')

    run_config(config, logger)


if __name__ == "__main__":
    main()
