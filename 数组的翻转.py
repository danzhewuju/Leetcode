def run():
    n = int(input())
    data = [int(x) for x in input().split()]
    if len(data) < 3: return True
    l, r = 0, len(data) - 1
    while  l < len(data)-1 and data[l+1] > data[l]:
        l += 1
    while r > 0 and data[r-1] < data[r]:
        r -= 1
    data = data[:l]+data[l:r+1][::-1]+data[r+1:]
    while l < len(data) -1 and data[l+1] > data[l]:
        l += 1
    if l == len(data) -1:
        return True
    else:
        return False
if run(): 
    print('yes')
else:
    print('no')
    

