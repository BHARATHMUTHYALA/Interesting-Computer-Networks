def bit_stuffing(data):
    stuffed_data="01111110"
    count=0
    for bit in data:
        stuffed_data+=bit
        if bit=='1':
            count+=1
        else:
            count=0

        if count==5:
            stuffed_data+='0'
            count=0

    stuffed_data+='01111110'
    return stuffed_data

def bit_unstuffing(stuffed_data):
    data=''
    count=0

    stuffed_data=stuffed_data[8:-8]

    i=0
    while i<len(stuffed_data):
        data+=stuffed_data[i]
        if stuffed_data[i]=='1':
            count+=1

        else:
            count=0

        if count==5 and i+1<len(stuffed_data) and stuffed_data[i+1]=='0':
            i+=1
            count=0

        i+=1

    return data


original_data="110111111111111110111"
stuffed_data=bit_stuffing(original_data)
unstuffed_data=bit_unstuffing(stuffed_data)

print(f"The original data is {original_data}")
print(f"The stuffed data is {stuffed_data}")
print(f"The unstuffed data is {unstuffed_data}")
