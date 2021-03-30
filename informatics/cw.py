n = int(input())
k = 0
p = pow(2, k)
while p <= n:
    print(p, end=' ')
    k+=1
    p = pow(2, k)
    
    