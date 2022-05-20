"""Given an array of integers and a value, determine if there are any two integers 
in the array whose sum is equal to the given value.
Return true if the sum exists and return false if it does not."""

def find_sum_of_two(A, val):
    """
    Runtime complexity: O(N)
    Space complexity: O(N)
    """
    vals_set = set(A)
    for el in vals_set:
        if val - el in vals_set: return True
            
    return False


if __name__ == "__main__":
    arr = [2, 7, 15, 11]
    val = 9
    res = find_sum_of_two(arr, val)
    print(res)
    assert res == True


    arr = [2, 8, 15, 11]
    val = 9
    res = find_sum_of_two(arr, val)
    print(res)
    assert res == False