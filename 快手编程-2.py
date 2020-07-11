# import collections
# def input_data():
#     n = int(input())
#     L = [int(input()) for _ in range(n)]
#     return L

# def sum_x(num):
#     res = 0
#     while num > 9:
#         res += (num%10)**2
#         num //= 10
#     res += num**2
#     return res

# def run():
#     L = input_data()
#     for i in range(len(L)):
#         res_dict = collections.defaultdict(int)
#         num = L[i]
#         res = num
#         while num != 1 and res_dict[num] == 0:
#             res_dict[num] = 1
#             num = sum_x(num)
#         if num == 1:
#             print("true")
#         else:
#             print("false")
#     return 

# run()
# # print(sum_x(123))

def sumOfSquares(n):
    flag = False
    htb = dict()
    while not htb.get(n):
        if n == 1:
            flag = True
            break
        tmp = 0
        while n!=0:
            tmp += (n%10) * (n%10)
            n = n//10
        n = tmp

    return flag

def sumBits():
    m = int(input())
    nums = []
    for i in range(m):
        tmp = int(input())
        nums.append(tmp)
    
    for n in nums:
        if sumOfSquares(n):
            print("true")
        else:
            print("false")



sumBits()