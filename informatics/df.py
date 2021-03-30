a = int(input())
b = int(input())
s = str(a)
cnt = 0
for i in range(len(s)):
    if int(s[i]) == b:
        cnt+=1
print(cnt)