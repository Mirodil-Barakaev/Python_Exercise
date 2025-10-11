def safe_divide(a, b):
    return a / b

s = "Hatolik"
def error_handler():
        return s

def run_if_safe(func, handler, a, b):
    if b != 0:
        return(func(a, b))
    else:
        handler()

print(run_if_safe(safe_divide, error_handler, 10, 2))