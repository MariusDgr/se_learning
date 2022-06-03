
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

def linked_list_palindromes():
    my_list = []
        
    while head:
        my_list.append(head.val)
        head = head.next
        
    # check for palindrome
    for i in range(0, int(len(my_list)/2)):
        if my_list[i] != my_list[len(my_list)-i-1]:
            return False
    return True

def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Optimal solution https://www.youtube.com/watch?v=yOzXms1J6Nk"""
        fast = head
        slow = head
        
        # find middle of list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True


if __name__ == "__main__":

    s = "abc"
    print(palindromic_substrings(s))

    s = "aaac"
    print(palindromic_substrings(s))

    my_list = [1, 2, 2, 1]
    print(my_list[:len(my_list)//2])
    print(my_list[-len(my_list)//2:].reverse())




