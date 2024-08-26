num = int(input("enter a number:"))
sum = 0
for i in range(1,num):
    if num%i==0:
        sum = sum + i
if sum == num:
    print("the num is perfect:")
else:
    print("not a perfect number")
    
# for i in range(5,51,5):
#     print(i)

n = int(input("enter a value: "))
count = 11
while count < n:
    count = count + 3
    print(count)
    
num = int(input("enter a number:"))
sum = 0
for i in range(1,num):
    if num%i==0:
        sum = sum + i
if sum == num:
    print("the num is perfect:")
else:
    print("not a perfect number")