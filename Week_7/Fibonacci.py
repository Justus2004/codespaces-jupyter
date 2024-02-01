def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def berechne_fibonacci_reihe(n):
    fibonacci_reihe = []
    for i in range(n):
        fibonacci_reihe.append(fibonacci(i))
    return fibonacci_reihe

n = 10
fibonacci_reihe = berechne_fibonacci_reihe(n)
print("Die ersten", n, "Fibonacci-Zahlen sind:", fibonacci_reihe)

