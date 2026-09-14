def is_pallindrome(text):
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()
    return cleaned_text == cleaned_text[::-1]

assert is_pallindrome("A man, a plan, a canal: Panama") == True, "Test 1"
assert is_pallindrome("race a car") == False, "Test 2"  
assert is_pallindrome("No 'x' in Nixon") == True, "Test 3"
assert is_pallindrome("a.") == True, "Test 4"
print("OK")