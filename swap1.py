# swapping variable with temporary variable

x = input("Enter value of x :")
y = input("Enter value of y :")

temp = x
x = y
y = temp

print("The value of x after swap :", x)
print("The value of y after swap :", y)