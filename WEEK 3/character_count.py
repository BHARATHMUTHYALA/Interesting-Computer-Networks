def count_character(input_string):
    input_string =  input_string.lower()
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = "Hello, World!"
result =  count_character(input_string)
print(result)
