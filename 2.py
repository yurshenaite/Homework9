import math

n = int(input())

while n > 2:
    n = math.sqrt(n)
    print('%.3f' % n)