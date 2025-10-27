def detect_stuffed_bits(data):
    count = 0
    positions = []
    
    for i in range(len(data)):
        if(data[i] == '1'):
            count += 1
        else:
            if count == 5: 
                positions.append(i)
                
            count = 0
    return positions 

stuffed_data = '011111010111110101111101011111010'
print("Stuffed data : ", stuffed_data)

stuffed_positions = detect_stuffed_bits(stuffed_data)
print("Stuffed Bit Positions(Index): ", stuffed_positions)

print("Stuffed bits Detected: ", [stuffed_data[i] for i in stuffed_positions])