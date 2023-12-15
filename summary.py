import logging
from systems.systems_buffer import load_buffer, read_buffer
from gpt import summary

buffer_dict = {}


def get_summary():

    try:
        load_buffer()
    except Exception as e:
        msg = f"Error loading buffer: {e}"
        logging.error(msg)

    try:
        msg = read_buffer()
        logging.info(f'Buffer is ready to process')
    except Exception as e:
        msg = f"Error reading buffer: {e}"
        logging.error(msg)

    try:
        logging.info(f'Starting summary')
        msg = summary(msg)
        logging.info(f'Summary is ready')
    except Exception as e:
        msg = f"Error summarizing buffer: {e}"
        logging.error(msg)

    return msg
