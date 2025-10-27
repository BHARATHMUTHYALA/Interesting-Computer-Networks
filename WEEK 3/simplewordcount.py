def word_character_count(text):
    words = text.split()
    total_words = len(words)
    total_characters = len(text)
    
    return total_words, total_characters
    
text = "Hello Bro welcome to code"
words , characters = word_character_count(text)
print("Total words: ", words)
print("Total characters: ", characters)
