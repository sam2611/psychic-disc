import collections
n = int(input())
r, g, y, b, o = map(int,input().split())
listcolor = []
for i in range(n):
    color=input()
    listcolor.append(color)
frequency = collections.Counter(listcolor)
r1 = frequency.get("red")
g1 = frequency.get("green")
y1 = frequency.get("yellow")
b1 = frequency.get("blue")
o1 = frequency.get("orange")

if r <= r1 and g <= g1 and y <= y1 and b <= b1 and o <= o1:
    print("Yes")
else:
    print("No")