def count_letters(s):
    big = 0
    small = 0
    for i in s:
        if i.isupper():
            big += 1
        elif i.islower():
            small += 1
    return big, small

print(count_letters("HelloWorld"))