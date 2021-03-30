import math
a = int(input())
cnt = 0
for i in range(1, int(math.sqrt(a))):
    if a % i == 0:
        cnt+=1

cnt *= 2
if a % int(math.sqrt(a)) == 0:
    cnt+=1
print(cnt)