def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "changed"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()