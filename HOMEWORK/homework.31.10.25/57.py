class Vec:
    def __init__(s,a):
        s.d={i:v for i,v in enumerate(a)if v}
    def __add__(s,o):
        r=s.d.copy()
        for i,v in o.d.items():
            r[i]=r.get(i,0)+v
        return Vec([r.get(i,0)for i in range(max(r)+1)])
    def __str__(s):
        return str(s.d)

v1=Vec([0,3,0,5])
v2=Vec([1,0,2,0])
print(v1+v2)
