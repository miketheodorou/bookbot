from collections import Counter

def count_words(text):
    return len(text.split())

def count_characters(text):
    return Counter(text.lower());