def run():
    m = int(input().strip())
    queue = []
    for i in range(m):
        tmp = [int(x) for x in input().strip().split()]
        if tmp[0] == 1: # insert
            a, b = tmp[1], tmp[2]
            queue.insert(a-1, str(b))
        elif tmp[0] == 2:
            a = tmp[1]
            del queue[a-1]
        else:
             print(' '.join(queue))
    return 

run()
    

            

