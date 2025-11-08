class Node:
    def __init__(s,v,c=None):
        s.v=v
        s.c=c or []
    def __repr__(s,l=0):
        r=" "*l+s.v+"\n"
        for i in s.c:r+=i.__repr__(l+1)
        return r

root=Node("A",[Node("B"),Node("C",[Node("D")])])
print(root)
