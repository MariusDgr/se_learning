def nextGreatestLetter(letters: list[str], target: str) -> str:
    n = len(letters)
    left = 0
    right = n - 1 
    mid = 0

    # edge case - last or above all
    if target >= letters[n - 1]:
        return letters[0]
    # edge case - first or below all
    if target < letters[0]:
        return letters[0]
    # BSearch solution: Time & Space: Log(N)

    while left <= right:
        mid = (left + right) // 2  # find the mid
        if target < letters[mid]:
            right = mid - 1
        elif target > letters[mid]:
            left = mid + 1
        else:
            while mid < n and letters[mid] == target: 
                mid += 1    
            return letters[mid]
        
    if letters[mid] < target:
        return letters[mid+1]
    else:
        return letters[mid]

if __name__ == "__main__":
    print(nextGreatestLetter(["e","e","e","k","q","q","q","v","v","y"], "f"))