
def wordBreak(s, d):
    """Bottom up approach with dp"""
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in d:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)] 
            if dp[i]:
                break
            
    return dp[0]



if __name__ == "__main__":

    s = "penpainappleapplepen"
    d = ["apple", "pen", "pain"]

    print(wordBreak(s, d))





