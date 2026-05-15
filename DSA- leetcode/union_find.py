n = 10
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa

union(1, 2)
union(2, 3)
union(4, 5)

print(find(3))   # ✅ Output: 1
