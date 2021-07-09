


t = int(input("Enter number of test cases: "))
print()
while (t != 0):
    m, n = map(int, input("Enter Lower and Upper Bounds: ").split())         #Input format: num1 num2
    prime=[True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False                   #Marks the numbers that are greater than or equal to p**2 and divisible by p
        p += 1

    for i in range(m, n + 1):
        if (prime[i])and i!=1:                    #Loop to print the unmarked numbers(prime numbers)
            print(i, end=" ")
        else:
            continue
    print()
    print()
    t -= 1

