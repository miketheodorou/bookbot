from collections import Counter

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read();

def count_words(text):
    return len(text.split())

def count_characters(text):
    return Counter(text.lower());

def sort_characters(dict):
    dicts = [{char: count} for char, count in dict.items()]
    dicts.sort(key=lambda d: list(d.values())[0], reverse=True)
    return dicts

def generate_char_output(char_dicts):
    return "\n".join([f"{char}: {count}" for char_dict in char_dicts 
                            for char, count in char_dict.items() 
                            if char.isalpha()])

def generate_report(file_path):
    contents = get_book_text(file_path)
    num_words = count_words(contents)
    characters = count_characters(contents)
    character_dicts = sort_characters(characters)
    char_output = generate_char_output(character_dicts)

    output = f'''
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{char_output}
============= END ===============
'''
    return output;
    