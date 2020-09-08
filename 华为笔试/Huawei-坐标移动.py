def run():
    line = input()
    direct = {'A':(0, -1),'D':(0, 1),'W':(-1, 0),'S':(1, 0)}
    line = line.split(';')
    loc = [0, 0]
    for w in line:
        if 2<= len(w) <= 3 and w[0] in direct and w[1:].isdigit():
            d = int(w[1:])
            print(w)
            p = w[0]
            dx, dy = d*direct[p][0], d*direct[p][1]
            loc = [loc[0]+dx, loc[1]+dy]
    print('{},{}'.format(loc[0], loc[1]))
    return 

if __name__ == "__main__":
    run()