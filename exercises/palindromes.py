
def palindromic_substrings(s):
    "O(N^2)"
    res = 0

    for i in range(len(s)):
        # Check odd palindromes
        res += count_palindromes(s, i, i)

        # Check even palindromes
        res += count_palindromes(s, i, i+1)

    return res

def count_palindromes(s, l, r):
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    return res

if __name__ == "__main__":

    s = "abc"
    print(palindromic_substrings(s))

    s = "aaac"
    print(palindromic_substrings(s))





