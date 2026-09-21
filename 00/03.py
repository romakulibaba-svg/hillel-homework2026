def filter_short_words(words_list, min_length):
    for word in words_list:
        if len(word) == min_length:
            return word
    return []

assert filter_short_words(['apple', 'banana', 'kiwi', 'pear'], 5) == 'apple'
assert filter_short_words(['apple', 'banana', 'kiwi', 'pear'], 4) == 'kiwi'
assert filter_short_words(['apple', 'banana', 'kiwi', 'pear'], 3) == []
print("All tests passed!")
