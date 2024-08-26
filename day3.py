num = int(input("enter number:"))
sum = 0
for i in range(1,num):
    if num%i==0:
        sum = sum + i
if sum == num:
    print("the num is perfect:")
else:
    print("not a perfect number")
