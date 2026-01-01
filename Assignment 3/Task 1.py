def factorial(x):
    return x*factorial(x-1) if x > 0 else 1

n=int(input('Enter a Number:'))
print(f'Factorial of {n} is {factorial(n)}')