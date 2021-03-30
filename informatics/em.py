n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    if i!=n-1 and a[i] > 0 < a[i+1]:
        print("YES")
        exit()
    elif i!=n-1 and a[i] < 0 > a[i+1]:
        print("YES")
        exit()
print("NO")