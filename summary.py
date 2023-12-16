import logging
from systems.systems_buffer import load_buffer, read_buffer, read_buffer_chat
from gpt import summary

buffer_dict = {}

def get_summary():
    try:
        load_buffer()
        logging.info('Buffer is ready to process')
    except Exception as e:
        msg = f"Error loading buffer: {e}"
        logging.error(msg)
        return msg

    try:
        buffer_content = read_buffer()
        logging.info('Starting summary')
        msg = summary(buffer_content)
        logging.info('Summary is ready')
        return msg
    except Exception as e:
        msg = f"Error reading or summarizing buffer: {e}"
        logging.error(msg)
        return msg


def get_chat_summary(chat_id):
    try:
        load_buffer()
        logging.info('Buffer is ready to process')
    except Exception as e:
        msg = f"Error loading buffer: {e}"
        logging.error(msg)
        return msg

    try:
        buffer_content = read_buffer_chat(chat_id)
        logging.info(f'Buffer content: {chat_id} {buffer_content}')
        logging.info(f'Starting chat summary')
        msg = summary(buffer_content)
        logging.info('Chat Summary is ready')
        return msg
    except Exception as e:
        msg = f"Error reading or summarizing chat buffer: {e}"
        logging.error(msg)
        return msg