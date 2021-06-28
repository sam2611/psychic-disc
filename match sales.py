
import collections
n = int(input().strip())

ar = list(map(int, input().split()))
frequency = collections.Counter(ar)
list1 = list(frequency.values())
result=0
r=0
for x in list1:
    if x%2==0:
        r=x/2
    else:
        r=(x-1)/2
    result=result+r
print(int(result))
