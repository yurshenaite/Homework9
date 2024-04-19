import math

n = int(input())

counter = 0
for i in range(1, int(math.sqrt(n)) + 1):
    for j in range(1, int(math.sqrt(n)) + 1):
        if i ** 2 + j ** 2 == n:
            counter += 1

print(counter // 2)