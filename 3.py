from math import log, floor


x = int(input())


MAX_K = floor(log(x, 3))
MAX_L = floor(log(x, 5))
MAX_M = floor(log(x, 7))
print(MAX_K, MAX_L, MAX_M)

result = []
for k in range(MAX_K):
    for l in range(MAX_L):
        for m in range(MAX_M):
            num = 3**k * 5**l * 7**m
            if num <= x:
                result.append(num)


print(sorted(set(result)))
