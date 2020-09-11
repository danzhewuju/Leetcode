def run():
    n, m = map(int, input().split())
    first, last = 0, 0
    # info = []
    dp = [1]*(n+1)
    dp[0] = 0
    go, leave = [], []
    for i in range(m):
        tmp = [int(x) for x in input().split()]
        # info.append(tmp)
        if tmp[1] == 1:
            go.append(tmp[0])
        else:
            leave.append(tmp[0])
    # 上班打卡的除了第一个外全部不是老板， 下班打卡的除了最后一个外，全部不是老板

    if len(go) > 1:
        for t in go[1:]:
            dp[t] = 0
    if len(leave) > 1:
        for t in leave[:-1]:
            dp[t] = 0

    # 现在需要讨论上班的第一个人,下班的最后一个人是不是老板
    go_flag = False
    for x in leave:
        if x not in go:  # 下班的记录里面存在一条记录上班里面没有, 上班第一个不是老板
            go_flag = True
            break
    leave_flag = False
    for x in go:
        if x not in leave:  # 上班的记录存在一条下班没有, 下班的最后一个不是老板
            leave_flag = True
            break
    print(go_flag, leave_flag)
    if go_flag:
        dp[go[0]] = 0
    if leave_flag:
        dp[leave[-1]] = 0

    res = [str(i) for i, x in enumerate(dp) if x == 1]
    ans = " ".join(res)
    print(ans)
    return


run()
