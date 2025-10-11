def g(nums, f1, f2): return [f1(i) if i%2==0 else f2(i) for i in nums]
print(g([1,2,3,4,5], lambda x:x*10, lambda x:x+1))