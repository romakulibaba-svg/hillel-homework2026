def find_unique_value(some_list):
    for element in some_list:
        if some_list.count(element) == 1:
            return element
    return None  

assert find_unique_value([1, 3, 1, 5, 5]) == 3, "Test 1"
assert find_unique_value([1, 1, 2, 2, 3]) == 3, "Test 2"
assert find_unique_value([4, 4, 6, 5, 5]) == 6, "Test 3"
assert find_unique_value([8, 7, 7, 9, 9]) == 8, "Test 4"
assert find_unique_value([1, 1, 2, 2]) is None, "Test 5"

print("OK")
