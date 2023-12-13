# systems_buffer.py
import logging
import json
# Initialize buffer as a dictionary object
buffer_dict = {}

# Writing buffer function, accepts chat ID and string message, and appends the message to the corresponding buffer
def write_buffer(chat_id, logmsg):
    global buffer_dict
    
    # Check if the chat ID exists in the buffer dictionary
    if chat_id not in buffer_dict:
        # If not, create a new buffer for the chat ID
        buffer_dict[chat_id] = []
    
    # Append the logged string message to the buffer of the corresponding chat ID
    buffer_dict[chat_id].append(logmsg)

# Function to convert all messages from a buffer into a single string
def read_buffer():
    global buffer_dict
    
    # Initialize an empty string to store the combined messages
    buffer_string = ""
    
    # Iterate over the buffer dictionary and concatenate all the messages
    for chat_id in buffer_dict:
        for logmsg in buffer_dict[chat_id]:
            buffer_string += logmsg + "\n" 
    return buffer_string

# Function to convert a chosen chat from the buffer into a string
def red_buffer_chat(chat_id):
    global buffer_dict
    
    # Initialize an empty string to store the messages of the chosen chat
    buffer_chat_string = ""
    
    # Check if the chat ID exists in the buffer dictionary
    if chat_id in buffer_dict:
        # Iterate over the messages of the chosen chat and concatenate them
        for logmsg in buffer_dict[chat_id]:
            buffer_chat_string += logmsg + "\n"
    return buffer_chat_string

# Function to get the number of chats stored in the buffer
def get_num_chats():
    global buffer_dict
    
    # Return the number of keys in the buffer dictionary
    return len(buffer_dict)

# Function to get the total number of messages stored in the buffer
def get_num_messages():
    global buffer_dict
    
    # Initialize a variable to store the count
    count = 0
    
    # Iterate over the buffer dictionary and sum up the lengths of all the buffers
    for chat_id in buffer_dict:
        count += len(buffer_dict[chat_id])
    
    return count

# Function to count the number of messages in a specific chat
def get_num_messages_in_chat(chat_id):
    global buffer_dict
    
    # Check if the chat ID exists in the buffer dictionary
    if chat_id in buffer_dict:
        # Return the length of the chat's buffer
        return len(buffer_dict[chat_id])
    else:
        # Return 0 if the chat ID does not exist
        return 0

# Function to retrieve the last 10 messages stored in a buffer as a string
def get_recap():
    all_messages = []
    
    for chat_id, buffer in buffer_dict.items():
        all_messages.extend(buffer)
    
    if len(all_messages) <= 10:
        return "\n\n".join(all_messages)
    else:
        return "\n\n".join(all_messages[-10:])

# Function to retrieve the last 10 messages from a specific chat stored in a buffer as a string
def get_recap_chat(chat_id):
    if chat_id in buffer_dict:
        buffer = buffer_dict[chat_id]
        if len(buffer) <= 10:
            return "\n\n".join(buffer)
        else:
            return "\n\n".join(buffer[-10:])
    else:
        return "Chat ID not found in buffer."
    
# Function to save the buffer to a file
def save_buffer(file_path='buffer.json'):
    global buffer_dict
    
    try:
        with open(file_path, 'w') as file:
            # Save the buffer dictionary as JSON
            json.dump(buffer_dict, file)
        logging.info(f"Buffer saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving buffer: {e}")

# Function to load the buffer from a file
def load_buffer(file_path='buffer.json'):
    global buffer_dict
    
    try:
        with open(file_path, 'r') as file:
            # Load the buffer dictionary from JSON
            loaded_buffer = json.load(file)
            buffer_dict.update(loaded_buffer)
        logging.info(f"Buffer loaded from {file_path}")
    except FileNotFoundError:
        logging.info(f"No buffer file found at {file_path}")
    except Exception as e:
        logging.error(f"Error loading buffer: {e}")

# Function to delete a specific chat and its buffer
def delete_buffer_chat(chat_id):
    global buffer_dict
    
    # Check if the chat ID exists in the buffer dictionary
    if chat_id in buffer_dict:
        # Delete the buffer of the corresponding chat ID
        del buffer_dict[chat_id]

# Function to delete the entire buffer
def delete_buffer():
    global buffer_dict
    
    # Clear the buffer dictionary
    buffer_dict.clear()

def send_buffer():
    pass