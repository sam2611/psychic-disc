arr = list(map(int, input().rstrip().split()))

size = len(arr)
arr.sort()
list1 = list(arr)

arr.remove(arr[0])
maxim = sum(arr)
list1.remove(list1[size-1])
minn = sum(list1)
print(minn, maxim)
