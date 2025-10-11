def i(f, n):
    def r():
        for _ in range(n): f()
    return r
def say(): print('ok')
i(say, 3)()