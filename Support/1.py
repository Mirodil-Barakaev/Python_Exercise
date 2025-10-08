def getMaxCount(n: int):
    a = n  
    b = n  

    while b >= 3:
        full = b // 3      
        a += full         
        b = b % 3 + full

    return a

print(getMaxCount(5))
