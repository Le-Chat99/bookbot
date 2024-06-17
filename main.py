def main():
    try:
        with open('books/frankenstein.txt') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print("File not found. Please check the path and ensure the file exists.") 
    
    words = file_contents.split()
    print(f"This book have: {len(words)} words")
    char_count= characters_counter(file_contents)
    for key, value in char_count.items():
        print(f"Have {value} of <{key}> char")
    
def characters_counter(file_contents):
    low_conts=file_contents.lower()
    unwanted_chars = [' ', '\n']
    chars_count= {}
    for char in low_conts:
        if char not in unwanted_chars:
            if char in chars_count:
                chars_count[char]+=1
            else:
                chars_count[char]=1
    sorted_chars_count = dict(sorted(chars_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars_count
    
main()