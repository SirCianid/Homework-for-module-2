import random

n = random.randint(3, 20)
result = ''
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += str(i) + str(j)
print(n)
print(result)