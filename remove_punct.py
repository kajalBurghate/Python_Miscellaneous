# remove punctuations from string

punctuactions = '''!()-{}[]:;'"\,<>./?@#$%^&*_`'''

my_str = input("Enter string :")

no_punct =""

for char in my_str:
    if char not in punctuactions:
        no_punct = no_punct + char

print(no_punct)