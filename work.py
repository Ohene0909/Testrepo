age = int(input("Enter the age.... "))
if age < 18:
    print("Minor")
elif age >=18 and age <60:
    print("Adult")
elif age >=60 and age <100:
    print("Elderly")
else:
    print("Unexpected")