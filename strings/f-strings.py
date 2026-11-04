while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0 or age >= 120:
            print("Please enter the correct format!")
            continue
        break
    except ValueError:
        print("Please enter a valid age number!")
print(f"your age is {age}")
