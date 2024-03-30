#right down mirror star print pattern

rows = int(input("Enter number of rows :"))

i = rows

while i >= 1:

    j = rows

    while j > i:

        print('', end = "")

        j = j - 1

    k = 1

    while k <= i:

        print("*", end="")

        k = k + 1

    print()

    i = i - 1