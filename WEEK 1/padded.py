def bit_stuffing(p,delimiter=''):
    x = ""
    for i in range(len(p)):
        x+=p[i]
        if(x.endswith('11111')):
            x+='0'
    return delimiter + x + delimiter

def pad(p):
    if(len(p)%8==0):
        return p
    else:
        return p + '0' * (8-len(p)%8) , p + '1' * (8-len(p)%8)
original_data='011110111110'
stuffed_data =  bit_stuffing(original_data)
zero_padded_data, one_padded_data = pad(stuffed_data)

print(f"Original Data: {original_data}")
print(f"Stuffed Data: {stuffed_data}")
print(f"Zero Padded Data: {zero_padded_data}")
print(f"One Padded Data: {one_padded_data}")
