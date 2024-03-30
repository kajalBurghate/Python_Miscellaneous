# power of 2 using anonymous functions

terms = int(input("Ebter a number :"))

result = list(map(lambda x : 2 ** x , range(terms)))

print("The total terms are : ", terms)

for i in range(terms):
    print("2 raised t power ", i, "is", result[i])
