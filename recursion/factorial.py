def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
