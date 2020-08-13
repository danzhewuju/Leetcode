import collections
a = input()
b = input()
# a = 'bcba'
# b = 'cbcb'
if len(a) != len(b):
    print(0)
else:
    dict_a = collections.Counter(a)
    dict_b = collections.Counter(b)
    if dict_a == dict_b:
        print(1)
    else:
        print(0)

