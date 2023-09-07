# 1.1 Implement a recursive funtion to calculate the factorial of a given number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result=factorial(int(input("Enter a number :")))
print(result)