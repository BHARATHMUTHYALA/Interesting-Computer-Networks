def calculate_parity(data):
    ones_count = data.count('1')

    return '0' if ones_count%2==0 else '1'

def dynamic_escape_char(data):

    possible_escape_chars=['1101101','1101010','01110110']
    sequence_count={esc: data.count(esc) for esc in possible_escape_chars}

    for escape_char in  sorted(sequence_count, key=sequence_count.get):
        if escape_char not in data:
            return escape_char
    least_used_character =  min(sequence_count, key=sequence_count.get) 

    
       
    modified_least_used_Character = least_used_character + '0'
    return modified_least_used_Character if modified_least_used_Character not in data else least_used_character

def bit_stuffing_with_error_detection(data):
    escape_char = dynamic_escape_char(data)
    stuffed_data, count='',0

    for bit in data:
        stuffed_data +=bit
        if bit=='1':
            count+=1
            if count==5:
                stuffed_data+=escape_char
                count=1
        else:
            count=0

        
    parity_bit = calculate_parity(data)
    flag_sequence='01111110'
    framed_data= flag_sequence + stuffed_data + parity_bit + flag_sequence

    return framed_data, escape_char, parity_bit

original_data = "111110111111000"
stuffed_data, escape_char , parity_bit = bit_stuffing_with_error_detection(original_data)

print(f"The original data is {original_data}")
print(f"The stuffed data is {stuffed_data}")
print(f"The escape character is {escape_char}")
print(f"The parity bit is {parity_bit}")