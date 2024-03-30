#check if string is palindrome or not

my_str = input("Enter string :")

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is Palindrome...")

else:
    print("The string is not Palindrome...")
