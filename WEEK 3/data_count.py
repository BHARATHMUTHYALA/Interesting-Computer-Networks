def count_character(text):
    character_count = {}
    for char in text:
        character_count[char] = character_count.get(char,0) + 1
    return character_count

text = "Hello, World! 123"
result = count_character(text)

print(result)
