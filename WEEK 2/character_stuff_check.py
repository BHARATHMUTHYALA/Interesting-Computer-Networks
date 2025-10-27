def character_stuffing(data, escape_char = '11110', flag='01111110'):
    special_chars = {'|', '!','?'}
    stuffed_data = ''
    for char in data:
        if char in special_chars:
            stuffed_data += escape_char + char
        else:
            stuffed_data += char
    return flag + stuffed_data +  flag

def character_unstuffing(stuffed_data, escape_char='11110', flag='01111110'):
    if stuffed_data.startswith(flag) and stuffed_data.endswith(flag):
        stuffed_data = stuffed_data[len(flag):-len(flag)]
    
    return stuffed_data.replace(escape_char, '')


def detect_stuffed_positions(stuffed_data, escape_char = '11110'):
    positions = []
    index = 0
    while index < len(stuffed_data):
        if stuffed_data[index : index + len(escape_char)] == escape_char:
            if index + len(escape_char) < len(stuffed_data) and stuffed_data[index +len(escape_char)] in {'|', '!', '?'}:
                positions.append(index + len(escape_char))
            index +=len(escape_char)
        else:
            index += 1
    return positions

data =  'Hello|World! How are you?'
escape_char = 'esc'
flag = 'flag'
stuffed_data =  character_stuffing(data, escape_char, flag)
print(f"Original data: {data}")
print(f"Stuffed data: {stuffed_data}")
print(f"Unstuffed data: {character_unstuffing(stuffed_data, escape_char, flag)}")
stuffed_positions =  detect_stuffed_positions(stuffed_data, escape_char)
print(f"Stuffed positions: {stuffed_positions}")
unstuffed_data = character_unstuffing(stuffed_data, escape_char, flag)
print(f"Destuffed data: {unstuffed_data}")

