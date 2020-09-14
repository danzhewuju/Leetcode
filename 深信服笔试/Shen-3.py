def run():
    T = int(input())
    for i in range(T):
        N = int(input())
        time_ = []
        max_length = 0
        for i in range(N):
            tmp = [int(x) for x in input().split()]
            max_length = max(max_length, max(tmp))
            time_.append(tmp)
        info = [0]*(max_length+1)
        for s, e in time_:
            for j in range(s, e+1):
                info[j] += 1
        ans = max(info)
        print(ans)

if __name__ == "__main__":
    run()
    pass