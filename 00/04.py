def count_elements(items_list):
    counts = {}
    for item in items_list:
        if item not in counts:
            counts[item] = 1  # Зустріли вперше
        else:
            counts[item] += 1  # Вже був, збільшуємо лічильник на 1
    return counts

assert co