fibonacci_memoization = {}
def fibonacci(n):#using memoization
    if n in fibonacci_memoization:
        return fibonacci_memoization[n]
    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_memoization[n] =  value
    return value


print(fibonacci(4))
