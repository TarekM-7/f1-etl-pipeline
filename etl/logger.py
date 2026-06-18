import logging

logging.basicConfig(
    format='[{levelname}] {asctime} | {message}',
    style='{',
    datefmt='%H:%M:%S',
    level=logging.INFO
)
def get_logger(name):
    return logging.getLogger(name)