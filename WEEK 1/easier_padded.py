def bit_stuffing(data):
    stuffed_data = ''
    count = 0
    for bit in data:
        stuffed_data += bit 
        if bit == '1':
            count+=1
            if count == 5:
                stuffed_data +='0'
                count = 0
        else:
            count =0
    return stuffed_data
def pad_to_byte_boundary(data, pad_type ='0'):
    if pad_type not in ('0','1'):
        raise valueError("pad type must be either '0' or '1'")
    pad_length = (8 - (len(data) % 8)) % 8
    padded_data = data + (pad_type * pad_length)
    return padded_data 


data  = "11111011111101111"
stuffed = bit_stuffing(data)
padded = pad_to_byte_boundary(stuffed)
print("Original Data : ", data)
print("After Bit Stuffing: ", stuffed)
print("After padding: ", padded)
