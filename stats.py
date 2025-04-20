def count_words(text):
    return len(text.split())

def count_characters(text):
    char_map = {}

    for character in text:
        char = character.lower()
        if(char in char_map):
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map