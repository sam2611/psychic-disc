Sum=0
n=0
a=1
b=2
# while a<=4e6 and b<=4e6:
while a<=4e6:
    if a%2==0:
        Sum = Sum + a
    n=a+b
    a=b
    b=n
# if b%2==0:
#     sum=sum+b
print(Sum)