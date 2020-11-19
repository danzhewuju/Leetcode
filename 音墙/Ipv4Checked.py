#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isIPv4Address(self , s ):
        # write code here
        if not s:
            return False
        ipv4 = [x for x in s.split('.')]
        if len(ipv4) != 4:
            return False
        for d in ipv4:
            for dd in d:
                if ord('0')<= ord(dd) <= ord('9'):
                    pass
                else:
                    return False
            if len(d) > 1 and d[0] == '0':
                return False
            if int(d) < 0 or int(d) > 255:
                return False
        return True


print(Solution().isIPv4Address("10.138.15.1"))