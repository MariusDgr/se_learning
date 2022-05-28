def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dp(n, fibs=None):
    if fibs is None:
        fibs = [1, 1]

    def _fib_dp():
        if len(fibs) == n:
            return fibs[-1]
        else:
            fibs.append(fibs[-2] + fibs[-1]) 
            return _fib_dp()

    return _fib_dp()

def fib_iter(n):
    if n == 1 or n == 2:
        return 1

    a = b = 1
    for i in range(2, n):
        new_val = a + b
        a = b
        b = new_val

    return b


if __name__ == "__main__":
    print(fib_recursive(25)) # takes a lot of time with n = 50 for example...

    print(fib_dp(50))

    print(fib_iter(50))