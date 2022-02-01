score = int(input("Enter the Score... "))
if score < 0  or score > 100:
    print("invalid input")
else:
    if score < 30:
        print("Grade = F")
    elif  score >= 30 and score < 45:
        print("Grade = C")
    elif score >= 45 and score < 60:
        print("Grade = B")
    elif score >=60 and score < 76:
         print("Grade = A")
    else:
         print("Grade = E")
