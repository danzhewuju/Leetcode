def run():
    s = input()
    info = [0]*128 # 标志  java 使用byte
    res = ""
    for c in s:
        t = ord(c)
        if info[t] == 0:
            info[t] = 1
            res += c
    print(res)
    return 

run()
