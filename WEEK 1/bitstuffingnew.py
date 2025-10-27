def bit_stuffing(p,flag='~',esc='A'):
    x=''
    for i in range(len(p)):
        x+=p[i]
        if(x.endswith('11111')):
            x+=esc
    return flag+ x + flag
original_data ='0111110111110'
stuffed_data = bit_stuffing(original_data)
print(f"Original Data : {original_data}")
print(f"Stuffed Data : {stuffed_data}")
