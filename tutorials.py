n = int(input("Enter the number... "))
for i in range(1,11):
    p = i*n
    if p%2==0:
        print(p)
    else:
        print(p+1)
