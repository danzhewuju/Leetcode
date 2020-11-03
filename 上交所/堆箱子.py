
def isBigger(big, small):
    if big[0] > small[0] and big[1] > small[1] and big[2] > small[2]:
        return True
    else:
        return False


def run():
    line = input()
    line = line[2:-2]
    data = []
    for d in line.split('],['):
        data.append([int(x) for x in d.split(',')])

    data = sorted(data, key=lambda x: (sum(x)))
    count =1
    last=data[0]
    for d in data[1:]:
        if isBigger(d, last):
            last=d
            count += 1
    print(count)
    return

run()

