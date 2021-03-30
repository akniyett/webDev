n = int(input())
k = 0
p = 1
if n == 1:
    print(0)
else:
    while p <= n:
        p *= 2
        k+=1
        if p >= n:
            print(k)
            break
    
    