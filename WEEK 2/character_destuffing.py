def character_stuffing(data, special_chars= '|', escape_char='esc'):
    data = data.replace(escape_char, escape_char + escape_char)
    data.replace(special_chars, escape_char + special_chars)
    return data

def character_unstuffing(stuffed_data, special_chars = '|', escape_char = 'esc'):
    unstuffed_data =  stuffed_data.replace(escape_char+special_chars, special_chars)
    unstuffed_data =  unstuffed_data.replace(escape_char+escape_char, escape_char)

    return unstuffed_data

original_code = "Text message | with special character"
stuffed_data =  character_stuffing(original_code)
unstuffed_data =  character_unstuffing(original_code)
print("Original code: ", original_code)
print("Stuffed data: ", stuffed_data)b
print("Unstuffed data: ", unstuffed_data)