#check armstrong number of n digits

num = int(input("Enter a number :"))

order = len(str(num))


sum = 0

temp = num
while temp > 0:
    digits = temp % 10
    sum += digits ** order 
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number" )

else:
    print(num, "is not an Armstrong number" )
