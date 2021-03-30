def xor(x, y):
    if x == y:
        return 0
    else:
        return 1
a, b = map(int, input().split())
print(xor(a, b))