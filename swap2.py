# swapping without temp variable


x = int(input("Enter value of x :"))
y = int(input("Enter value of y :"))

x = x + y
y = x - y
x = x - y

print("The value of x after swap :", x)
print("The value of y after swap :", y)