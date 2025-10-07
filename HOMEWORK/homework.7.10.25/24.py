def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrome_number(121))