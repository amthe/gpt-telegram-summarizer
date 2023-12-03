# Simple function to get .env API keys
def get_key(key):
    with open('.env', 'r') as file:
        for line in file:
            if not line.strip().startswith('#') and '=' in line:
                file_key, value = line.strip().split('=', 1)
                if file_key == key:
                    # print(f'\n {key} : {value}\n')
                    return value
    return None