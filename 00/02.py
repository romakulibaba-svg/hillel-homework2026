def elementes(some_list):
    for i in range(len(some_list) - 1):
        if some_list[i] == some_list[i + 1]:
            return True
    return False