import re
import pytest

def find_longest_word(sentence: str):
    without_punctuation = re.sub("[-!\.\?'\"]", "", sentence)
    words = re.split(" ", without_punctuation)
    longest = ["", 0]
    for word in words:
        word_len = len(word)
        if word_len > longest[1]:
            longest[0] = word
            longest[1] = word_len
    return longest

def find_shortest_word(sentence: str):
    without_punctuation = re.sub("[-!\.\?'\"]", "", sentence)
    words = re.split(" ", without_punctuation)
    shortest = [words[0], len(words[0])]
    for word in words:
        word_len = len(word)
        if word_len < shortest[1]:
            shortest[0] = word
            shortest[1] = word_len
    return shortest


#Unit tests below, run sentense_parser.py with pytest to execute
# In Terminal: pytest --junitxml=results.xml sentence_parser.py
long_data = [("A sentence.", ["sentence", 8]), ("A super-sentence.", ["supersentence", 13])]
short_data = [("Some short sentence.", ["Some", 4]), ("Another short sentence.", ["short", 5])]
@pytest.mark.parametrize("test_string, expected", long_data)
def test_longest_word_parser(test_string, expected):
    assert find_longest_word(test_string)

@pytest.mark.parametrize("test_string, expected", short_data)
def test_shortest_word_parser(test_string, expected):
    find_shortest_word(test_string)