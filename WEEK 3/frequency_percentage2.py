from collections import Counter
def char_frequency_percentage(text):
    cleaned_text = text.replace(" ","")
    total_chars = len(cleaned_text)
    
    frequency = Counter(cleaned_text)
    
    print(f"{'Character':^10} | {'Count':^5} | {'Percentage':^10}")
    print("-" * 30)
    for char, count in frequency.items():
        percentage = (count / total_chars) * 100
        print(f"{char:^10} | {count:^5} | {percentage:>9.2f}%")
        
input_text = input("Enter a string: ")
char_frequency_percentage(input_text)
