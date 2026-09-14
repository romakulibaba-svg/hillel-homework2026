def add_one(some_list):
    num_str = str(int("".join(map(str, some_list))) + 1)
    return [int(char) for char in num_str]

assert add_one([1, 2, 3]) == [1, 2, 4], "Test 1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test 2"
assert add_one([0]) == [1], "Test 3"
assert add_one([9]) == [1, 0], "Test4"

print("OK")
