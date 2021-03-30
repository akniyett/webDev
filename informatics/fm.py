n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    if 0 != i !=n-1 and a[i-1] < a[i] > a[i+1]:
        cnt+=1
print(cnt)