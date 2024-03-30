#count number of each vowels from string

vowels = 'aeiou'

ip_str = input("Enter String :")

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels, 0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)