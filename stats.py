from collections import Counter

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read();

def count_words(text):
    return len(text.split())

def count_characters(text):
    return Counter(text.lower());

def sort_characters(dict):
    dicts = []
    for key in dict:
        print(key)
        item = {}
        item[key] = dict[key]
        dicts.append(item)
    dicts.sort(key=lambda d: list(d.values())[0], reverse=True)
    return dicts

def generate_report(file_path):
    contents = get_book_text(file_path)
    num_words = count_words(contents)
    characters = count_characters(contents)
    character_dicts = sort_characters(characters)

    output = f'''
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
'''
    for char_dict in character_dicts:
      for character, count in char_dict.items():
          if character.isalpha():
              output += f"{character}: {count}\n"
    output += '============= END ==============='
    return output;
    