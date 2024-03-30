# print binary number using recursion

def ConvertToBinary(n):
    if n > 1:
        ConvertToBinary(n//2)
    print(n % 2, end = '')

num = int(input("Enter number :"))

ConvertToBinary(num)

print()

#print("Binary converion is :", num)