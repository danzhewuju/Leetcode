def compare(A_num, B_num):
    max_length = max(len(A_num), len(B_num))
    while len(A_num) < max_length: A_num.append("0")
    while len(B_num) < max_length: B_num.append("0")
    for j in range(max_length):
        if int(B_num[j]) > int(A_num[j]):
            return True
        if int(B_num[j]) < int(A_num[j]):  # 需要进一步的加快运算
            return False
    return False
 
def run():
    n = int(input())
    for i in range(n):
        L = input().strip().split()
        u = L[0]
        v = L[1]
        u, v = u.split('.'), v.split('.')
        if compare(u, v):
            print("true")
        else:
            print("false")
    return
         
run()