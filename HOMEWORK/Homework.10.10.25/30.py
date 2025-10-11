def k(funcs,v): return [f(v) for f in funcs]
print(k([lambda x:x+1,lambda x:x**2],5))