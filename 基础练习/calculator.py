def f1score_cal():
    precision, recall = [float(x) for x in input().split()]
    f1score = 2 * precision * recall / (precision + recall)
    f1score = round(f1score, 4)
    return f1score


if __name__ == '__main__':
    while True:
        print(f1score_cal())
