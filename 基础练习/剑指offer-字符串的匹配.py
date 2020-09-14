import re
def isMatch(s: str, p: str) -> bool:

    # 判断s字符串是否和p的正则表达式匹配
    m, n = len(s), len(p)
    dp = [[False]*(m+1) for _ in range(n+1)]
    # 初始化
    dp[0][0] = True
    for i in range(1, m+1): # 没有正则匹配的情况
        dp[0][i] = False
    first_start = True
    for j in range(1, n+1): # 空字符串的匹配情况
        if p[j-1] == '*' and first_start:
            dp[j][0] = True
        else:
            first_start = False
            dp[j][0] = False
    for j in range(1, m+1):
        for i in range(1, n+1):
            if s[j-1] == p[i-1]: dp[i][j] = dp[i-1][j-1]
            if p[i-1] == '.' : dp[i][j] = dp[i-1][j-1]
            if p[i-1] == '*': # 重点讨论*的情况
                # dp[i][j] = dp[i-1][j] or dp[i][j-1]  
                dp[i][j] = i > 2 and dp[i-3][j-1] or p[i-2] in [s[j-1], '.'] and dp[i-1][j-2]
    return dp[-1][-1]
    # res = re.match('c*a*b', 'aab')

    # return True if res else False

print(isMatch('aab', 'c*a*b'))

     