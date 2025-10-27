def character_stuffing(data, escape_char='11110', flag = '01111110'):
    special_chars = { '|', '!', '?'}
    stuffed_data = ''
    for char in data:
        if char in special_chars:
            stuffed_data+=escape_char + char
        else:
            stuffed_data+=char
    return flag + stuffed_data + flag


def character_destuffing(stuffed_data, escape_char='11110', flag = '01111110'):
    if stuffed_data.startswith(flag):
        stuffed_data =  stuffed_data[len(flag):]
    if stuffed_data.endswith(flag):
        stuffed_data =  stuffed_data[:-len(flag)]
    return stuffed_data.replace(escape_char,'')

data = 'Hello|World! How are you?'
escape_char = 'esc'
flag = 'flag'
stuffed_data = character_stuffing(data, escape_char, flag)
print(f"Original data: {data}")
print(f"Stuffed data: {stuffed_data}")
destuffed_data =  character_destuffing(stuffed_data ,escape_char, flag)
print(f"Destuffed data: {destuffed_data}")
