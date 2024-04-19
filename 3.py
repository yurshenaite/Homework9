n = int(input())

splitter = []
for i in range(2, n+1):
    if n % i == 0:
        splitter.append(i)

splitter_min = min(splitter)
print(splitter_min)