def climbStairsRecursive(n: int) -> int:
        if n == 1 or n == 0:
            return 1
        
        return climbStairsRecursive(n-1) + climbStairsRecursive(n-2)

def climbStairsDP(n):
    if n == 0:
        return 1 

    prev = [1]
    for i in range(1, n+1):
        total = 0
        for j in [1, 2]:
            if i - j >= 0:
                total += prev[i - j]
        prev.append(total)
    return prev[n]

if __name__ == "__main__":
    print(climbStairsRecursive(2))
    print(climbStairsDP(2))
