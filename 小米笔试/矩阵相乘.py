import numpy as np
def run():
    M, K, N = map(int, input().strip().split())
    A, B = [], []
    for i in range(M):
        tmp = [int(x) for x in input().strip().split()]
        A.append(tmp)
    for i in range(K):
        tmp = [int(x) for x in input().strip().split()]
        B.append(tmp)
    # res = [[0]*N for _ in range(M)]
    A = np.array(A)
    B = np.array(B)
    C = np.matmul(A, B)
    for i in range(M):
        for j in range(N):
            if j == N-1:
                print(C[i][j], end='\n')
            else:
                print(C[i][j], end=' ')
    return 
    

run()

    