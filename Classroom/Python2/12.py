def contains(toshmat, eshmat):
    return toshmat in eshmat
print(contains(5, [1, 2, 3, 4, 5]))    
print(contains("a", ("b", "c", "d")))  
print(contains(10, {10, 20, 30}))      
