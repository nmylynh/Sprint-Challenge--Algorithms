def fibonacci(n):
    # Write your code here
    if n < 0:
        raise ValueError("There is no fibonacci sequence that can be returned at 0.")
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)