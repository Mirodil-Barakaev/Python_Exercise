def is_palindrome_string(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome_string("Level"))