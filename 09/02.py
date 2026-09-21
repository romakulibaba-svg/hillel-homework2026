def difference(*args):
    if not args:
        return 0
    min_value = min(args)
    max_value = max(args)
    return round(max_value - min_value, 2)


assert difference(1, 2, 3, 4, 5) == 4, "Test 1"
assert difference(10.5, 2.3, 7.8) == 8.2, "Test 2"
assert difference(-5, -10, -3) == 7, "Test 3"
assert difference() == 0, "Test 4"
print("OK")
