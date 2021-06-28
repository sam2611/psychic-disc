n = int(input())
s = set(map(int, input().split()))
N=int(input())
for x in range(N):
    task=input().split()
    if task[0]=="pop":
         s.pop()
    elif task[0]=="remove":
         s.remove(int(task[1]))
    elif task[0]=="discard":
         s.discard(int(task[1]))
    
print(sum(s))
