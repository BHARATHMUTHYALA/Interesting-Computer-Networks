def character_frequency_percentage(text):
    total_characters = len(text)
    character_count = {}
    frequency_percentage =  {}
    for char in text:
        if char in character_count:
            character_count[char] +=1
        else:
            character_count[char] = 1
    for char, count in character_count.items():
        frequency_percentage[char] = (count / total_characters) * 100
    return frequency_percentage

text = "Hello"
result = character_frequency_percentage(text)
print(result)

text2 = "NET"
result2 = character_frequency_percentage(text2)
print(result2)

