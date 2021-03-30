n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    if i!=n-1 and a[i] < a[i+1]:
        cnt+=1
print(cnt)