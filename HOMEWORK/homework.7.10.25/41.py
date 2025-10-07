def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i.isalpha() and i not in vowels:
            count += 1
    return count

print(count_consonants("Hello"))