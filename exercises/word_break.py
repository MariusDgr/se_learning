
def dp_word_break(s, d):
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

def recursive_word_break(s, d):
    n = len(s)
    for i in range(0, n+1):
        fw = s[0:i]
        sw = s[i:n-1]
        if fw in d:
            if (sw in d) or (len(sw) == 0):
                return True
            else:
                return recursive_word_break(sw, d)

    return False

if __name__ == "__main__":

    s = "penpainappleapplepen"
    d = ["apple", "pen", "pain"]

    print(dp_word_break(s, d))
    print(recursive_word_break(s, d))






