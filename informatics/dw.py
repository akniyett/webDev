n = int(input())
if n==1:
    print("YES")
else:
    while n>=0:
        if n/2 == 1:
            print("YES")
            break
        elif n/2 < 1:
            print("NO")
            break
        else:
            n /= 2