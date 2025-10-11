def f(names, t): return [t(i) for i in names]
print(f(['Eshmat','Toshmat','Mirodil'], lambda x: x.upper()))