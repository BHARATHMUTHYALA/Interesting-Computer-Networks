def bit_stuffing(data):
    stuffed_data,count='',0
    for bit in data:
        stuffed_data+=bit
        if bit=='1':
            count+=1
            if count==5:
                stuffed_data+='0'
                count=0
        else:
            count=0
    return stuffed_data

def custom_bit_stuffing(data , delimiter='01111110'):
    data = data.replace(delimiter,"")

    stuffed_data = bit_stuffing(data)

    framed_data= delimiter + stuffed_data + delimiter

    return framed_data

test_data="111110111111000"
stuffed_output=custom_bit_stuffing(test_data)
print("Stuffed data:",stuffed_output)

