
def factorial(n):
    print("Called")
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def factorialMemo(n, prev=None):
    if prev is None:
        prev = [1, 1]

    def compfactorial():
        print("Called")
        
        if (len(prev)-1) == n:
            return prev[n] 
        else:
            new_val = (n - (len(prev) - 2)) * prev[-1]
            prev.append(new_val)
            return compfactorial()

    return compfactorial()
        
    
if __name__ == "__main__":
    print(factorial(5))


    print(factorialMemo(5))