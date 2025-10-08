a = 1
def func():
    global a
    a = 2
    print(a)
func()
print(a)