#display half pyramid pattern of star 

rows = int(input("Enter number of rows :"))

for i in range(rows + 1, 0, -1):

    for j in range(0, i - 1):

        print("*", end = "")

    print(" ")
