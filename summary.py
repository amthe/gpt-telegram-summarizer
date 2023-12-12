from systems.systems_buffer import load_buffer, read_buffer
from gpt import summary

buffer_dict = {}

def get_summary():
	msg = load_buffer()
	msg = read_buffer()
	msg = summary(msg)
	return msg
