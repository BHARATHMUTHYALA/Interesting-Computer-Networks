def count_character_case_insensitive(text):
    text = text.lower()
    character_count = {}
    for char in text:
        if char.isalnum():
            if char in character_count:
                character_count[char] +=1
            else:
                character_count[char] = 1
    return character_count

def count_word_characters(text):
    words = text.split()
    framed_data = []
    for word in words:
        word_length =  len([char for char in word if char.isalnum])
        framed_data.append(f"{word_length}:{word}")
    return framed_data

text1 = "Hello, World"
result1 =  count_character_case_insensitive(text1)
print("Character count (case insensitive): ", result1) 
text2 =  "Hello 123 World!"
result2 =  count_word_characters(text2)
print("Framed Data: ")
for data in result2:
    print(data)
