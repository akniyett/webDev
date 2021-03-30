n = int(raw_input())
arr = map(int, raw_input().split())
m = max(arr)
ans = -1e9
for i in range(n):
    if m > arr[i] >= ans:
        ans = arr[i]
print(ans)