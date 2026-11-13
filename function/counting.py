total = 0
count = 0

number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    total = total + number
    count = count + 1
    number = int(input("Enter a number (-1 to stop): "))

print("Total:", total)
print("Numbers entered:", count)
