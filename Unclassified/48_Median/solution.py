n = int(input())
l = list(map(int, input().split()))
l.sort()
a = len(l)
print(int(l[a//2]) if a & 1 else int((l[a//2-1]+l[a//2])/2))