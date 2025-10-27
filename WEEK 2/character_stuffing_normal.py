def character_stuffing(data):
    flag = '10101010'
    escape_character = '11100'
    stuffed_data = ''
    count_ones =  0
    
    for bit in data:
        if bit == '1':
            count_ones += 1
        else:
            count_ones = 0
        stuffed_data+=bit
        if count_ones == 5:
            stuffed_data += escape_character
            count_ones = 0
            
    stuffed_data = flag +stuffed_data + flag
    return stuffed_data
        
original_data = '111101110111110111111101110'
stuffed_data = character_stuffing(original_data)
print(original_data)
print(stuffed_data)