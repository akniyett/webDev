n = int(input())
A = []
B = []  
for i in range(n):
    name = str(raw_input())
    A.append(name)
    score = float(raw_input())
    B.append(score)
m = min(B)
ans = 1e9
for i in range(n):
    if m < B[i] <= ans:
        ans = B[i]
res = []
for i in range(n):
    if B[i] == ans:
        res.append(A[i])
res = sorted(res)
for i in range(len(res)):
    print(res[i])
        
