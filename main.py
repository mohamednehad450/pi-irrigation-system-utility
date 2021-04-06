import atexit

from config import load_config, run_config
from utils import log_with_timestamp, exit_handler

atexit.register(exit_handler)


def main():

    logfile = 'log.txt'
    def logger(m): log_with_timestamp(m, logfile)

    run_config(
        load_config('config.json', 'schema.json'),
        logger)


if __name__ == "__main__":
    main()
