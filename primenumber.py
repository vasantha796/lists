#1. print only prime digits in a number #12421
n1=12421
prime=[2,3,5,7]
for i in str(n1):
    if int(i) in prime:
        print(i,end=" ")

# 2.palidrome
n1="12421"
n2=n1[::-1]
if n1==n2:
    print("palindrome")
else:
    print("not a palindrome")    

# 3.even digits in a number

n1=12421
for i in str(n1):
    if int(i)%2==0:
        print(i,end=" ")

# 2,4,2

# 4.perfect number #single
n1=6
sum=0
for i in range(1,n1):
    if n1%i==0:
        sum+=i

if sum==n1:
    print("perfect number") 

else:
    print("not a perfect number")               

# 5.print perfect number from 1 to 100

for n1 in range(1,101):
    sum=0
    for i in range(1,n1):
        if n1%i==0:
         sum+=i

    if sum==n1:
        print(n1,end=" ")   #6,28 