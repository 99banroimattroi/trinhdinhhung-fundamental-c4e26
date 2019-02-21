print("         Calculate n!")

n = int(input("Enter a number: "))

if n < 0:
    print("Error ! (n) is the natural numbers")
    print("    ---Please try again---")
else:
   
    k=1

    for i in range(1,n+1):
        k *= i

    print("The factorial of",n,"is:" ,k)