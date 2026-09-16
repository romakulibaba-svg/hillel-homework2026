from __future__ import annotations
def popular_words(text: str, words: list[str]) -> dict[str, int]:
    
    for punct in [',', '.', ';', '!', '?']:
        text = text.replace(punct, '')
        
    words_lower = text.lower().split()
    return {word: words_lower.count(word.lower()) for word in words}

assert popular_words('''When I was a child, I spoke as a child, I understood as a child, I thought as a child''', ['child', 'I']) == {'child': 4, 'I': 4}, "Test 1"
assert popular_words('''Hello world! This is a test. Hello again.''', ['hello', 'test', 'world']) == {'hello': 2, 'test': 1, 'world': 1}, "Test 2"
assert popular_words('''Python is great. Python is fun. I love Python.''', ['python', 'is', 'fun']) == {'python': 3, 'is': 2, 'fun': 1}, "Test 3"
print("OK")