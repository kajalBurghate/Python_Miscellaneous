# calculator by using functions

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation.")
print("1.Addition")
print("2.Substraction")
print("Multiplication")
print("Division")

while True:
    choice = input("Enter Choice(1/2/3/4) :")

    if choice in ('1', '2', '3','4'):
        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))

        except ValueError:
            print("Invalid Input. Please enter a number .")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (Yes/ No) :")

        if next_calculation == "No":
            break
        
        else:
            print("Invalid Input....")

