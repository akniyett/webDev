n = int(input())
k = 2
while n:
    if n % k == 0:
        print(k)
        break
    else:
        k+=1