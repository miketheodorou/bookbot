from stats import count_words

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read();
    
def main():
    contents = get_book_text('./books/frankenstein.txt')
    num_words = count_words(contents)
    print(f"{num_words} words found in the document")

main()