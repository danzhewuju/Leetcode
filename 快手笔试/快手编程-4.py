content = [x for x in input().split()]
insert = [x for x in input().split()]
gap = 4 
p , q = 0, 0
res = []
while p < len(content):
    if p != 0 and p % gap == 0 and q < len(insert):
        res.append(insert[q])
        q += 1
    res.append(content[p])
    p += 1
if q < len(insert):
    res += insert[q:]
res = " ".join(res)
print(res)

