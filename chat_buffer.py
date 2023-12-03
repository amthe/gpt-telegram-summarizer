# Initialize Buffer as a list object
buffer_list = []
# Writing buffer function, accepts string message and appends it to a list
def buffer(logmsg):
    global buffer_list
    # appends logged sring message to a list
    buffer_list.append(logmsg)