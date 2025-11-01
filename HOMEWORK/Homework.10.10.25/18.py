def h(f):
    print(f.__name__, f())
def hi():
    return 'salom'
h(hi)