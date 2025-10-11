def e(s): return (lambda x: x.upper()) if s[0].lower() in 'aeiou' else (lambda x: x.lower())
print(e('apple')('salom'))