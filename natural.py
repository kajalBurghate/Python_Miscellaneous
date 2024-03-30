# find sum of natural numbers

num = int(input("Enter a number :"))

if num < 0:
    print("Enter a psitive number.")

else:
    sum = 0
    while(num > 0):
        sum = sum + num
        num = num - 1

    print("The sum is :", sum)