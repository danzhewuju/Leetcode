def myPow(x: float, n: int) -> float:
        if n == 0:
            return 1
        P_n = n if n > 0 else -n
        # 对于大数需要进行特殊的处理
        # 指数级的扩展
        res = 1
        while P_n:
            if P_n & 1:
                res *= x
            x *= x
            P_n >>= 1
        return res if n > 0 else 1/res

print(myPow(0.001, 1000))