n = int(input())
s = str(n)
m = len(s)
sum = 0
for i in range(len(s)):
    sum += int(s[i]) * pow(2, m-1)
    m -= 1
print(sum)