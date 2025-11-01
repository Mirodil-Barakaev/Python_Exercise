def make_multiplier(operation):
    if operation == 'square':
        return lambda num: num * num
    elif operation == 'cube':
        return lambda num: num * num * num
    elif operation == 'double':
        return lambda num: num * 2

res = make_multiplier('cube')
print(res(5))