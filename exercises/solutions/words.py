import os

_PATH = '../resources'
_FILE = 'lorem.txt'


def read_file(filepath: str = os.path.join(_PATH, _FILE)) -> str:
    with open(filepath, 'r') as file:
        contents = file.read()
    return contents

def count_lines(filepath: str = os.path.join(_PATH, _FILE), include_empty: bool = False) -> int:
    with open(filepath, 'r') as file:
        num_lines = 0
        for line in file:
            if include_empty:
                num_lines += 1
            else:
                if line.strip():
                    num_lines += 1
        return num_lines

def count_non_empty_lines(filepath: str = os.path.join(_PATH, _FILE)) -> int:
    with open(filepath, 'r') as file:
        num_lines = 0
        for line in file:
            num_lines += 1
        return num_lines

def count_words(contents: str) -> int:
    word_list = contents.split()
    num_words = len(word_list)
    return num_words

def count_chars(contents: str, include_eol: bool = False) -> int:
    if include_eol:
        num_chars = len(contents)
    else:
        num_chars = len(contents.replace('\n', ''))
    return num_chars

def count_unique_words(contents: str) -> int:
    contents = contents.lower().replace('.', '').replace(',', '')
    word_list = contents.split()
    word_set = set(word_list)
    return len(word_set)

def count_word_occurences(contents: str) -> int:
    # Remove punctuation and special characters
    text = contents.lower()
    words = text.split()
    words = [word.strip(".,!?\"':;()[]") for word in words]

    # Count the occurrences of each word
    words_counts = {}
    for word in words:
        words_counts[word] = words_counts.get(word, 0) + 1

    # Sort the words based on their occurences
    sorted_words_counts = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words_counts

def count_sentences(contents: str) -> int:
    return len(contents.split('.')) - 1 # Remove the last dot

def result(filepath: str = None) -> None:
    filepath = os.path.join(_PATH, _FILE) if filepath is None else filepath
    contents = read_file(filepath)
    num_lines = count_lines(filepath, include_empty=True)
    num_non_empty_lines = count_lines(filepath, include_empty=False)
    num_sentences = count_sentences(contents)
    num_words = count_words(contents)
    num_unique_words = count_unique_words(contents)
    num_chars = count_chars(contents, include_eol=True)
    num_non_eol_chars = count_chars(contents, include_eol=False)
    words_occurs = count_word_occurences(contents)

    print(f"File {filepath} contains:")
    print(f"  - Lines (including empty): {num_lines}")
    print(f"  - Lines (excluding empty): {num_non_empty_lines}")
    print(f"  - Sentences: {num_sentences}")
    print(f"  - Words (all): {num_words}")
    print(f"  - Words (unique): {num_unique_words}")
    print(f"  - Chars (including all): {num_chars}")
    print(f"  - Chars (excluding EOLs): {num_non_eol_chars}")

    print(f"\nThe 10 most frequent words in the file are:")
    for word, count in words_occurs[:10]:
        print(f"  - {word}: {count}")
