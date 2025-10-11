def j(s):
    if s=='+': return lambda a,b:a+b
    if s=='-': return lambda a,b:a-b
    if s=='*': return lambda a,b:a*b
    if s=='/': return lambda a,b:a/b
print(j('*')(3,4))