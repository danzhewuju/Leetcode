def run():
    def dfs(idx, h_d, p_d, v_d):
        nonlocal count
        if idx == Sum:
            count += 1
            return
        map_set = set()
        if idx % 2 == 0:  # 偶数
            if 0 <= idx-2 < Sum:
                map_set.add(Map[idx-2])
        else:  # 奇数
            if 0 <= idx-1 < Sum:
                map_set.add(Map[idx-1])
            if 0 <= idx-2 < Sum:
                map_set.add(Map[idx-2])
        if h_d > 0 and 0 not in map_set:
            Map[idx] = 0
            dfs(idx+1, h_d-1, p_d, v_d)
        if p_d > 0 and 1 not in map_set:
            Map[idx] = 1
            dfs(idx+1, h_d, p_d-1, v_d)
        if v_d > 0 and 2 not in map_set:
            Map[idx] = 2
            dfs(idx+1, h_d, p_d, v_d-1)
        return 
    h, p, v = map(int, input().split(','))
    Sum = h+p+v
    count = 0
    Map = [0]*(h+p+v)  # 0, 1, 2
    dfs(0, h, p, v)
    print(count)
    return


run()
