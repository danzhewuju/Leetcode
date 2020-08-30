def run():
    m,n = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    min_, max_ = min(nums), max(nums)
    is_ = 1
    for i in range(n):
        if i > 1 and nums[i] < nums[i-1]:
            is_ = 0
    res = 0
    for i in range(1, m):
        l = i
        for j in range(2, m+1):
            r,last, flag = j, -(10**9+7), True
            if max_ < l or r < min_: res += is_
            for k in range(n):
                if nums[k] > r or nums[k] < l:
                    if last == -(10**9+7) or last <= nums[k]:
                        last = nums[k]
                    else:
                        flag = False
                        break
            if flag: res += 1
    print(res)
    return 

if __name__ == "__main__":
    run()