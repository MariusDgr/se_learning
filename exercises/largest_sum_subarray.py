
from cmath import inf


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

if __name__ == "__main__":

    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sub_array_of_size_k(arr))






