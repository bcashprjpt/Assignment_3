
n = int(input("Enter a number: "))
def factorial(num):
    if (num<=1):
        return 1
    else:
      fact = num * factorial(num-1)
    return fact
res = factorial(n)
print("factorial of ",n," is: ",res) 
