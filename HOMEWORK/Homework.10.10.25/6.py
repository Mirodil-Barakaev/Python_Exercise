def apply(func:callable,val1:int,val2:int): 
    return func(val1,val2)
print(apply(lambda x,y:x*y,val1=5,val2=10))

