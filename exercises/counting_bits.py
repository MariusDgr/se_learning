
def countBits(n: int) -> list[int]:
    res = []
    for i in range(n+1):
        res.append(sum([int(v) for v in bin(i)[2:]]))
    return res

def countBitsDp(n: int) -> list[int]:
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


if __name__ == "__main__":
    n = 5
    print(countBitsDp(n))

    print(bin(2)[2:])