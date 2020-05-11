while True:
    A=int(input("Enter an Integer"))
    if A>=0 and A<=1000:
        break
    else:
        print("Invalid Entry!")
a=b=flag=0
for a in range (1,A):
    for b in range (1,A):
        if (a**2 + b**2)==A and a<=b:
            print(a,",",b)
            flag=1
if flag==0:
    print("No pairs")
