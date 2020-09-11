def run():
    s = input()
    dp = [0]*4
    if len(s) < 8:
        print('Irregular password')
        return 
    for c in s:
        if ord('0')<=ord(c)<=ord('9'):
            dp[0] = 1
        elif ord('A') <= ord(c) <= ord('Z'):
            dp[1] = 1
        elif ord('a') <= ord(c) <= ord('z'):
            dp[2] = 1
        else:
            dp[3] = 1
    if sum(dp) == 4:
        print('Ok')
        return 
    else:
        print('Irregular password')
        return 


while True:
    try:
        run()
    except: 
        break