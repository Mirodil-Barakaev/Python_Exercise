char = input("Enter a character: ")
k = int(input("Enter a number: "))


a=chr((ord(char) + k))

if ord(a) > 90:
    a = chr((ord(a) - 26))
print(a)