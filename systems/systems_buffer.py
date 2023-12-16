import logging
import json

# Initialize buffer as a dictionary object
buffer_dict = {}

# Writing buffer function, accepts chat ID and string message, and appends the message to the corresponding buffer
def write_buffer(chat_id, logmsg):
    buffer_dict.setdefault(chat_id, []).append(logmsg)

# Function to convert all messages from a buffer into a single string
def read_buffer():
    return "\n".join(logmsg for chat_id in buffer_dict for logmsg in buffer_dict[chat_id])

# Function to convert a chosen chat from the buffer into a string
def read_buffer_chat(chat_id):
    return "\n".join(buffer_dict[chat_id]) if chat_id in buffer_dict else ""

# Function to get the number of chats stored in the buffer
def get_num_chats():
    return len(buffer_dict)

# Function to get the total number of messages stored in the buffer
def get_num_messages():
    return sum(len(buffer_dict[chat_id]) for chat_id in buffer_dict)

# Function to count the number of messages in a specific chat
def get_num_messages_in_chat(chat_id):
    return len(buffer_dict.get(chat_id, []))

# Function to retrieve the last 10 messages stored in a buffer as a string
def get_recap():
    all_messages = [logmsg for chat_id in buffer_dict for logmsg in buffer_dict[chat_id]]
    return "\n\n".join(all_messages[-10:]) if all_messages else ""

# Function to retrieve the last 10 messages from a specific chat stored in a buffer as a string
def get_recap_chat(chat_id):
    buffer = buffer_dict.get(chat_id, [])
    return "\n\n".join(buffer[-10:]) if buffer else "Chat ID not found in buffer."

# Function to save the buffer to a file
def save_buffer(file_path='buffer.json'):
    try:
        with open(file_path, 'w') as file:
            json.dump(buffer_dict, file)
        logging.info(f"Buffer saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving buffer: {e}")

# Function to load the buffer from a file
def load_buffer(file_path='buffer.json'):
    try:
        with open(file_path, 'r') as file:
            loaded_buffer = json.load(file)
            buffer_dict.update(loaded_buffer)
        logging.info(f"Buffer loaded from {file_path}")
    except FileNotFoundError:
        logging.info(f"No buffer file found at {file_path}")
    except Exception as e:
        logging.error(f"Error loading buffer: {e}")

# Function to delete a specific chat and its buffer
def delete_buffer_chat(chat_id):
    buffer_dict.pop(chat_id, None)

# Function to delete the entire buffer
def delete_buffer():
    buffer_dict.clear()

def send_buffer():
    pass
