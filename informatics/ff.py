a = int(input())
s = 0
while a >= 1:
    s = 10 * s + a % 10
    a //= 10
print(s)