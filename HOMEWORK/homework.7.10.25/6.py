def is_in_range(n, start, end):
    if n >= start and n <= end:
        return True
    else:
        return False

print(is_in_range(5, 1, 10))