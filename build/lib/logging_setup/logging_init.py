import logging
import sys
from logging_setup import CustomisedJSONFormatter

def log_init(log, debug=False, plain_text_log=False, stream_handler=sys.stdout):
    log_handler = logging.StreamHandler(stream_handler)

    if plain_text_log:
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    else:
        formatter = CustomisedJSONFormatter()
    log_handler.setFormatter(formatter)
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    log.addHandler(log_handler)
