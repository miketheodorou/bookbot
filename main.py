from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read();
    
def main():
    contents = get_book_text('./books/frankenstein.txt')
    num_words = count_words(contents)
    num_characters = count_characters(contents)
    print(num_characters)
    print(f"{num_words} words found in the document")

main()