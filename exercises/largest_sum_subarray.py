
def max_sub_array_of_size_k(arr):
    """Kadane's algorithm"""
    current_max = arr[0]
    global_max = arr[0]
    for i in range(1, len(arr)):
        if current_max < 0:
            current_max = arr[i]
        else: 
            current_max = current_max + arr[i]

        if global_max < current_max: 
            global_max = current_max

    return global_max


def maxSubArray(self, nums: List[int]) -> int:
    
    g_max = nums[0]
    l_max = nums[0]
    
    for n in nums[1:]:
        if l_max <= 0 and n > l_max:
            l_max = n
        else:
            l_max += n
        
        if l_max > g_max:
            g_max = l_max
            
    return g_max

if __name__ == "__main__":

    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sub_array_of_size_k(arr))






