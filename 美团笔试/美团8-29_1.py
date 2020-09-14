def run():
    n = int(input())
    s = input().strip()
    l, r = 0, n - 1
    flag = False
    while l < n and (s[l] != 'T' or flag == False) :
        if s[l] == 'M':
            flag = True
        l += 1
    flag = False
    while r >= 0 and (s[r] != 'M' or flag == False):
        if s[r] == 'T':
            flag = True
        r -= 1
    res = s[l+1:r]
    print(res)
    return 

while True:
    try:
        run()
    except:
        break
